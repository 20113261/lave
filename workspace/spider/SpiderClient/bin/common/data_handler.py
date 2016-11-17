#!/usr/bin/env python
#coding=UTF8

'''
    data_handler
'''
import re
import json
import lxml.html as HTML
import lxml.etree as etree
#import lxml.html.soupparser as soupparser

# Structure of json_string
def jsonStruct(json_str, depth = 0, attr_flag = True):

    tmp_depth = depth
    attrFlag = attr_flag

    json_dict = json_str

    struct = ''
    
    # 初始时刻，如果参数是str，应该先转化为dict
    if tmp_depth == 0:
        if type(json_str).__name__ == 'str':
            try:
                json_dict = json.loads(json_str)
            except Exception, e:
                print 'Json Loads Error: ' + str(e)
                return struct
        elif type(json_str).__name__ == 'dict':
            json_dict = json_str
        else:
            print 'Json Loads Error: Wrong json_str Type, only str or dict supported'
            return struct
    
    #for i in range(0, depth):
        #struct = struct + '  '

    if type(json_dict).__name__ == 'dict':
        for k, v in json_dict.iteritems():
            for i in range(0,depth):
                 struct = struct + '  '
            if type(v).__name__ == 'dict':
                struct = struct + k + ':\n' + jsonStruct(v, depth = tmp_depth + 1, attr_flag = attrFlag)
            else:
                struct = struct + k + ': ' + jsonStruct(v, depth = tmp_depth + 1, attr_flag = attrFlag)

    elif type(json_dict).__name__ == 'list':
        for i in range(len(json_dict)):
            struct += '\n'
            for j in range(0,depth):
                struct = struct + '  '
            struct += str(i) + '\n'
            for j in range(0,depth):
                struct = struct + '    '
            struct = struct + jsonStruct(json_dict[i], depth = tmp_depth + 2, attr_flag = attrFlag)

    else:
        struct = struct + str(json_dict) + '\n'

    return struct


def find_json(json_str = '', path = '', debug_flag = True):
    #找到一个json结构数据的子元素
    if type(json_str).__name__ == 'str':
        try:
            json_str = json.loads(json_str)
        except Exception,e:
            error = 'Loads Json Fail, Json_str should have a dict format'
            if debug_flag == True:
                return error
            else:
                return None

    elif type(json_str).__name__ != 'dict':
        error = 'Loads Json Fail, Json_str should have a dict format'
        if debug_flag == True:
            return error
        else:
            return None

    try:
        return eval(str(json_str) + str(path))
    except Exception,e:
        error = 'Find Path Failed, No Target Path, Try jsonStruct(json_str)'
        if debug_flag == True:
            return error
        else:
            return None

    return None

def regexs(page = '', expression = '', debug_flag = True):

    #返回匹配正则表达式的元素列表
    try:
        return expression.findall(page)
    except Exception,e:
        error = 'Wrong Paras Type, Expression Should be a Valid re.compile instance'
        if debug_flag == True:
            return error
        return None

def regex(page = '', expression = '', index = 0, debug_flag = True):
    #匹配正则表达式，返回指定index的元素
    try:
        elements = expression.findall(page)
    except Exception,e:
        error = 'Wrong Paras Type, Expression Should be a Valid re.compile instance'
        if debug_flag == True:
            return error
        else:
            return None

    try:
        return elements[int(index)]
    except Exception,e:
        error = 'List Index Out of Range'
        if debug_flag == True:
            return error
        else:
            return None

def treeStruct(html_str = '', depth = 0, attr_flag = True):
               
    tmp_depth = depth
    attrFlag = attr_flag

    if type(html_str).__name__ == 'str':
        tree = HTML.fromstring(html_str)
    else:
        tree = html_str
        
    struct = ''

    if tree == None:
        print 'GetTree Failed'
        return struct
                                                                                                                                                       
    for i in range(0, depth):
        struct = struct + '\t'

    attrs = tree.attrib
    attr_str = ''

    if attr_flag == True:
        for k,v in attrs.iteritems():
            attr_str = attr_str + ' ' + k + '=' + v

    struct = struct + '<' + str(tree.tag) + attr_str + '>' + '\n'

    if len(tree) > 0:
        for child in tree:
            struct = struct + treeStruct(child, depth = tmp_depth + 1, attr_flag = attrFlag)
    
    return struct

def getTree(html_str, charset = 'utf-8'):

    try:
        tree = TreeHandler(html_str, charset = 'utf-8')
        return tree
    except Exception, e:
        error = ''
        return None

class TreeHandler(object):

    def __init__(self, html_str = '', charset = 'utf-8'):
        self.__charset = charset
        self.__debug = False
        self.__tree = self.tree(html_str)

    def tree(self, html_str):

        charset = self.__charset

        try:
            tree = HTML.fromstring(html_str.decode(charset))

        except Exception,e:
            print 'GetTree Error: ' + str(e)
            return None

        return tree

    def struct(self):
        
        return treeStruct(self.__tree)

    def xpath(self, path):
        #find nodes, return a node list

        tree = self.__tree

        if type(tree).__name__ == 'str':
            try:
                tree = HTML.fromstring(tree)
            except Exception, e:
                pass

        try:
            nodes = tree.xpath(path)
            return nodes

        except Exception, e:
            print 'GetNodeByXpath Error: ' + str(e)

        return None

    def get_element_by_id(self, id):

        tree = self.__tree

        if type(tree).__name__ == 'str':
            try:
                tree = HTML.fromstring(tree)
            except Exception, e:
                pass
        
        try:
            return tree.get_element_by_id(id)
        except Exception, e:
            pass

        return None

    def find_class(self, clazz):

        tree = self.__tree

        if type(tree).__name__ == 'str':
            try:
                tree = HTML.fromstring(tree)
            except Exception, e:
                pass

        try:
            return tree.find_class(clazz)
        except Exception, e:
            pass

        return None

    def encode(self, data, charset = None):
                
        if charset == None:
            charset = self.__charset

        if type(data).__name__  == 'str':
            try:
                return data.encode(charset)
            except:
                return data
        elif type(data).__name__ == 'list':
            edata = []
            for sdata in data:
                if type(data).__name__ == 'str':
                    try:
                        edata.append(sdata.encode(charset))
                    except:
                        edata.append(sdata)
                else:
                    edata.append(sdata)
            return edata
        else:
            return data

if __name__ == "__main__":
    
    #test
    json_str = '{"title":"test","author":"tester","content":["json","regex","xpath"]}'
    
    print 'JSON TEST'
    print jsonStruct(json_str)
    print '-------------'
    print find_json(json_str,'["content"][0]')
    print '-------------'
    
    import re
    re_str = 'this is a text_miaoji_string'
    expression = re.compile('_(.*?)_',re.S)

    print 'REGEX TEST'
    print str(regex(re_str,expression,0))
    print '-------------'
    print str(regex(re_str,expression,1))
    print '-------------'
    print str(regexs(re_str,expression))
    print '-------------'


    html_str = '<html><body id="1">abc<div class="first">123</div>def<div>456</div>ghi</body></html>'

    tree =  getTree(html_str = html_str)
    
    print 'XPATH TEST'
    print tree.struct() 
    print '-------------'

    print tree.get_element_by_id('1')
    print '-------------'
    print tree.find_class('first')
    print '-------------'
    print tree.xpath('//body/text()')
