#!/usr/bin/env python
#coding:utf-8

import os
import re
import sys
import pdb
import json
import traceback
import ConfigParser
from pprint import pprint
from logger import logger

from lxml import html
from re import compile

class FieldObj:
    '''
    FieldObj对象主要有三大功能：
    1. 对其赋值时是对其_val赋值（__setattr__）
    2. 可以递归地对其生成属性（__setattr__）
    3. 对其的任何方法调用都会被路由到_val上（__getattr__）
    废话不多说，我们拿一个具体的例子来说：

    >>> obj = FieldObj()        # 生成FieldObj实例
    >>> obj.dept = 'this is dept'   # 对属性赋值会被路由到对属性对象的_val赋值
    >>> obj.dept._val           # dept属性成为FieldObj实例，其_val属性为刚才赋值的字符串
    'this is dept'
    >>> obj.dept                # 调用obj.dept.__repr__，路由到obj.dept._val.__repr__
    'this is dept'
    >>> obj.dept.split()        # obj.dept.split被路由到obj.dept._val.split
    ['this', 'is', 'dept']
    >>> obj.dept[:4]            # 取下标调用obj.dept.__getitem__，进而被路由到obj.dept._val.__getitem__
    'this'
    >>> for x in obj.dept[0]: print x  # 迭代会调用obj.dept.__iter__，进而路由到obj.dept._val.__iter__
    t
    >>> obj.dept + ' and dest!' # obj.dept.__add__被路由到obj.dept._val.__add__
    'this is dept and dest!'
    >>> setattr(obj, 'dept.time.am.hour', '10:10')      # 任意深度的属性赋值，其每个属性都是一个FieldObj实例
    >>> obj.dept.time           # 打印obj.dept.time._val，默认是None
    None
    >>> obj.dept.time.am.hour   # 打印obj.dept.time.am.hour._val
    '10:10'
    >>> obj.dept                # 与此同时obj.dept._val的值并没有丢失
    'this is dept'
    >>> setattr(obj, 'dept.time.pm.day', '2016-05-18')  # 在obj.dept.time上新增pm属性
    >>> obj.dept.time.pm.day    # 打印obj.dept.time.pm.day._val
    '2016-05-18'

    基本来说，这个类实现的功能在上面的doc里已经完全体现出来了，配合README.md食用效果更佳。

    '''
    _val = None
    def __setattr__(self, attr, val):
        '''
        __setattr__在对实例进行属性赋值时调用。
        如果attr参数是以.号分隔的字符串，则递归赋值，即：
        
        >>> obj = FieldObj()
        >>> setattr(obj, 'a.b.c.d', 'we reached d')

        经过上式调用后，obj实例便具有了obj.a.b.c.d这么深的属性，其中
        a、b、c、d属性都是FieldObj对象实例，而'we reached d'字符串挂在
        obj.a.b.c.d._val上。

        默默吐个槽，如果想实现obj.a.b.c.d = ''这样直接的赋值，恐怕只有用
        ast进行元编程，但是我只想说，Perl语言里是默认可以进行任意深度的
        赋值的，虽然只是哈希表：$hash->{a}{b}{c}{d} = ''.

        '''

        if attr == '_val':
            self.__dict__['_val'] = val
            return

        attr_split = attr.split('.', 1)
        fieldname, rem = attr_split[0], attr_split[1:]
        fieldobj = self.__dict__.setdefault(fieldname, FieldObj())
        if rem:
            setattr(fieldobj, rem[0], val)
        else:
            fieldobj.__dict__['_val'] = val

    def __getattr__(self, attr):
        '''
        __getattr__会在FieldObj对象实例取属性失败时进行调用，比如说：

        >>> obj = FieldObj()
        >>> hasattr(obj, '__add__')
        False
        >>> obj._val = 2
        >>> obj + 1
        3

        在上面的例子里，obj实例并没有__add__对象，但是在进行中缀加号
        运算时对__add__的调用被路由到其_val属性上了，于是最终进行1+1
        运算并返回2.

        '''

        return getattr(self._val, attr)

class ExtractParser(FieldObj, object):
    debug = False
    def __init__(self, config_path=None):
        '''
        ExtractParser包装了标准库ConfigParser的ConfigParser类。
        在实例初始化时一个ConfigParser对象。
        '''
        self.__config = ConfigParser.ConfigParser()
        if config_path:
            self.__config.read(config_path)

    def __getattr__(self, attr):
        '''
        __getattr__在self实例取attr失败后触发，为self.__config.get(attr, opt)
        提供了一种人性化的调用方式：self.attr.opt:

        >>> import io
        >>> sample_config = """
        ... [ext]
        ... dept = xpath
        ... """
        >>> parser = ExtractParser()
        >>> parser._ExtractParser__config.readfp(io.BytesIO(sample_config))
        >>> parser._ExtractParser__config.get('ext', 'dept')
        'xpath'
        >>> parser.ext.dept
        'xpath'

        如上例所示，parser包装的ConfigParser对象可以直接以取属性的方式得到。
        若parser.__config没有attr域，那么会尝试调用parser.__config.attr。

        >>> import io
        >>> sample_config = """
        ... [ext]
        ... dept = xpath
        ... """
        >>> parser = ExtractParser()
        >>> parser.readfp(io.BytesIO(sample_config))
        >>> parser.get('ext', 'dept')
        'xpath'

        上例说明了这种行为的用法。
        '''
        if self.__config.has_section(attr):
            return _GetAttr(lambda option: self.__config.get(attr, option))
        else:
            try:
                return getattr(self.__config, attr)
            except AttributeError:
                logger.error('ExtractParser :: ExtractParser instance doesn\'t have property: %s'
                             % attr)
                raise AttributeError

    def parse(self, content):
        '''
        外部调用接口。content为html或json字符串。
        '''
        type = self.__config.get('basic', 'type')
        extract_meth = getattr(self, type + '_extract')

        extract_sections = self.__config.get('basic', 'options')
        for extract_section in extract_sections.split():
            has_flag = self.__config.has_option(extract_section, 'flag')
            skip = has_flag and self.__config.get(extract_section, 'flag') not in content
            if skip: continue

            extract_meth(extract_section, content)
            std_section = extract_section + '_std'
            if self.__config.has_section(std_section):
                # TODO: exception handler
                self.re_std(std_section)

    pat_path = re.compile('''(?:[^'"&]|'[^']*'|"[^"]*")+''')
    xnode_fmt = lambda self, xnode:  '<%s %s>' % (xnode.tag, ' '.join('%s="%s"' % (k,v) for k,v in xnode.items()))
    def xpath_extract(self, section, html_data):
        '''
        用xpath对指定的section进行解析。
        
        '''
        xroot = html.fromstring(html_data)
        # pnode_xpath shall be '.' as default xpath
        p_xpath = self.__config.get(section, 'pnode') if self.__config.has_option(section, 'pnode') else '.'
        p_xnodes = xroot.xpath(p_xpath)
        for field, xpath in self.__config.items(section):

            # skip if flag is `pnode` section
            if field in ('flag', 'pnode'):
                continue

            # print debug info if `self.debug` is set True
            if self.debug:
                print '\n{token}> {field}: {xpath}'.format(token='-'*10, field=field, xpath=xpath)
                p_xnode_fmt = [self.xnode_fmt(x) if isinstance(x, html.HtmlElement) else x for x in p_xnodes]
                print self.debug_info_t.format(indent='', leng=len(p_xnodes), node=p_xnode_fmt, path=p_xpath)

            p_xvalues = []
            for p_xnode in p_xnodes:
                # p_xnode is the list of HtmlElement objects which come from root.xpath(pnode)
                # we split xpath with `&&`, using a regexp `self.pat_path`
                xpathes = self.pat_path.findall(xpath)
                p_xvalue = self._xpath_recursive(p_xnode, xpathes)
                p_xvalues.append(p_xvalue)
            if p_xpath == '.':
                p_xvalues = p_xvalues[0]
            setattr(self, field, p_xvalues)

    jnode_fmt = lambda self, jnode: '<list>' if isinstance(jnode, list) else '<dict: %s>' % sorted(jnode.keys())[0]
    def json_extract(self, section, json_data):
        '''
        结构与`xpath_extract`基本相同，从json和指定的section中清洗数据。
        '''
        
        #TODO: exception catch!
        jroot = json.loads(json_data)
        p_jpath = self.__config.get(section, 'pnode') if self.__config.has_option(section, 'pnode') else ''
        p_jnodes = self._xjson(jroot, p_jpath)
        for field, jpath in self.__config.items(section):
            if field in ('flag', 'pnode'):
                continue

            if self.debug:
                print '\n{token}> {field}: {path}'.format(token='-'*10, field=field, path=jpath)
                p_jnode_fmt = [self.jnode_fmt(x) if isinstance(x, list) or isinstance(x, dict) else x for x in p_jnodes]
                print self.debug_info_t.format(indent='', leng=len(p_jnodes), node=p_jnode_fmt, path=p_jpath)

            p_jvalues = []
            for p_jnode in p_jnodes:
                jpathes = self.pat_path.findall(jpath)
                p_jvalue = self._xjson_recursive(p_jnode, jpathes)
                p_jvalues.append(p_jvalue)
            if not p_jpath:
                p_jvalues = p_jvalues[0]
            setattr(self, field, p_jvalues)

    def re_std(self, std_section):
        '''
        对std section进行解析，使用正则表达式进行数据的过滤和提取。
        
        >>> import io
        >>> config = """
        ... [std]
        ... dept = compile('\d\d(?=:\d\d)')
        ... """
        >>> parser = ExtractParser()
        >>> parser.readfp(io.BytesIO(config))
        >>> parser.dept = [[['10:11', ['12:13']], '14:15'], '16:17']
        >>> parser.re_std('std')
        >>> parser.dept
        [[['10', ['12']], '14'], '16']

        '''
        for field, regex in self.__config.items(std_section):
            pattern = eval(regex)
            field_split = field.split('.')
            fieldobj = self
            for fd in field_split[:-1]:
                fieldobj = fieldobj.__dict__[fd]

            last_fd = field_split[-1]
            if hasattr(fieldobj, last_fd):
                fieldobj = fieldobj.__dict__[last_fd]
                fieldobj._val = self._map_recursive(fieldobj._val, pattern)
                continue

            last_val = self._map_recursive(fieldobj._val, pattern)
            setattr(fieldobj, last_fd, last_val)
                
    debug_info_t = '{indent}{leng} elements: {node}\t<={path}'
    def _xpath_recursive(self, pnode, xpathes, depth=1):
        '''
        递归取xpath。若最终的数据是节点对象而不是字符串则调用text_content方法。
        '''
        if not xpathes:
            if isinstance(pnode, html.HtmlElement):
                # TODO: encode?
                pnode = pnode.text_content()
            return pnode
        snodes = pnode.xpath(xpathes[0].strip())
        
        # self.debug为True时，打印出跟踪的解析xpath的信息。
        if self.debug:
            snodes_fmt = [self.xnode_fmt(node) if isinstance(node, html.HtmlElement) else node for node in snodes]
            print self.debug_info_t.format(indent=' '*4*depth, leng=len(snodes), node=snodes_fmt, path=xpathes[0])
        return [self._xpath_recursive(snode, xpathes[1:], depth+1) for snode in snodes]
        
    def _map_recursive(self, val, pattern):
        '''
        递归对嵌套列表里的每一个字符串进行正则表达式处理，若正则表达无法匹配则过滤掉这条字符串。
        在正则匹配异常时用None进行占位，并且在回溯时对None进行过滤。
        '''
        if not isinstance(val, list):
            try:
                return pattern.search(val).group()
            except:
                return None
        res_ = [self._map_recursive(x, pattern) for x in val]
        return filter(lambda x: x is not None, res_)

    def _xjson(self, jnode, jpath):
        '''
        解析json路径
        '''
        try:
            evalled = eval('jnode' + jpath)
        except KeyError:
            return [None]
        if not isinstance(evalled, list):
            return [evalled]
        return evalled

    def _xjson_recursive(self, jnode, jpathes, depth=1):
        '''
        递归解json
        '''
        if not jpathes:
            return jnode
        s_jnode = self._xjson(jnode, jpathes[0].strip())
        s_jnode = filter(lambda x: x is not None, s_jnode)

        # 调试信息
        if self.debug:
            jnode_fmt = [self.jnode_fmt(x) if isinstance(x, list) or isinstance(x, dict) else x for x in s_jnode]
            print self.debug_info_t.format(indent=' '*4*depth, leng=len(s_jnode), node=jnode_fmt, path=jpathes[0])
        return [self._xjson_recursive(x, jpathes[1:], depth+1) for x in s_jnode]

    def test(self, content, path, method='xpath'):
        '''
        测试接口
        输入为文本形式下的html/json、xpath/jpath路径，并指定解析方法xpath/json
        '''
        orig_debug, self.debug = self.debug, True
        if method == 'xpath':
            root = html.fromstring(content)
            xpathes = self.pat_path.findall(path)
            xpath_val = self._xpath_recursive(root, xpathes, 0)
            self.debug = orig_debug
            return xpath_val

        elif method == 'json':
            root = json.loads(content) if isinstance(content, basestring) else content
            jpathes = self.pat_path.findall(path)
            jpath_val = self._xjson_recursive(root, jpathes, 0)
            self.debug = orig_debug
            return jpath_val



class _GetAttr:
    def __init__(self, lambda_fun):
        self.lambda_fun = lambda_fun

    def __getattr__(self, attr):
        return self.lambda_fun(attr)


def ErrorException(return_key):
    '''
    异常捕捉装饰器
    用法可参考README.md
    '''
    def inner(fun):
        def wrapper(*args, **kws):
            try:
                return fun(*args, **kws)
            except:
                filename = fun.__code__.co_filename
                tbs = traceback.format_exc().splitlines()
                for i in xrange(len(tbs)-1, -1, -1):
                    if filename in tbs[i]:
                        exc_lineno = tbs[i].strip()
                        exc_line = tbs[i+1].strip()
                        exc_info = tbs[-1].strip()
                        break

                startline = fun.func_code.co_firstlineno
                excline = int(re.search('line (\d+)', exc_lineno).group(1))

                with open(filename) as crt_file:
                    instance_name = None
                    pat_instance_name = re.compile('(\w+)\s*=\s*ExtractParser(?:\.ExtractParser)??\([^)]*\)')
                    for line in crt_file:
                        match_instance_name = pat_instance_name.search(line)
                        if match_instance_name:
                            instance_name = match_instance_name.group(1)
                            break

                    if not instance_name:
                        logger.error( '%s: cannot find instance of Parser.Parser!' % filename)

                    crt_file.seek(0)
                    field_name = None
                    pat_field_name = re.compile('%s\.(\w+)' % instance_name)
                    for line in crt_file.readlines()[startline:excline]:
                        match_field_name = pat_field_name.search(line)
                        if match_field_name:
                            field_name = match_field_name.group(1)

                if not field_name:
                    field_name = 'cannot catch fieldname somehow!'
                error_log = '{filename}: MIGHT BE {field_name} Error!\n\terror_lineno: {exc_lineno}\n\terror_line: {exc_line}\n\terror_info: {exc_info}'
                logger.error(error_log.format(**locals()))

                res = sys.exc_info()[2].tb_next.tb_frame.f_locals.get(return_key)
                return res

        return wrapper

    if callable(return_key):
        fun, return_key = return_key, 'tickets'
        return inner(fun)
    return inner


if __name__ == '__main__':

    text = 'demo/ctrip'
    type = '.json'
    parser = ExtractParser(text + '.cfg')
    html_text = open(text + type).read()
    #parser = ExtractParser()
    #print parser.test(html_text, './/*[contains(@class, "r2-pkg pack")] && .//*[@class="[ js-filter-price ]"]')
    parser.debug = True
    parser.parse(html_text)
    #for k, v in parser.__dict__.items():
    #    pprint((k,v))
    pdb.set_trace()

    #text = 'hoteltravelEN.cfg'
    #parser = ExtractParser(text)
    #json_data = open('hoteltravelEN.json').read()
    #parser.debug = True
    #parser.parse(json_data)
    #for k, v in parser.__dict__.items():
    #    print k
    #    pprint(v, width=1)
    #pdb.set_trace()
