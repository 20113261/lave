from fabric.api import local, task, lcd, env, run, roles, execute, cd, put
import datetime


env.roledefs = {
    'dev': ['root@10.10.187.129'],
    'test_spider': ['spider@10.10.95.70', 'spider@10.10.84.225', 'spider@10.10.48.27'],
}


def _hello():
    local('echo "hello"')


def _build_dir():
    path = 'build_{0}'.format(datetime.datetime.now().strftime('%Y-%m-%d-T%H%M%S'))
    local('mkdir {0}'.format(path))
    return path


def _submodule_update():
    local('git submodule init')
    local('git submodule update')


def _build_old_spider(tag):
    local('git clone http://gitlab.uc.online/spider/slave_develop_new.git')
    local('cd slave_develop_new')
    with lcd('slave_develop_new'):
        local('git checkout {tag}'.format(tag=tag))
        _submodule_update()
        local('git submodule status')
        local('mkdir workspace/spider/SpiderClient/bin/start/slavepid')


def _build_new_spider(tag):
    local('mkdir tmp')
    with lcd('tmp'):
        local('git clone http://gitlab.uc.online/spider_new/Spider.git')
        with lcd('Spider'):
            local('git checkout {tag}'.format(tag=tag))
            _submodule_update()
            local('git submodule status')
    local('scp -r tmp/Spider/src/mioji slave_develop_new/workspace/spider/SpiderClient/bin/mioji')


@task
def build(old_ver, new_ver, path=None):
    if not path:
        path = _build_dir()
    with lcd(path):
        local('pwd')
        _build_old_spider(old_ver)
        _build_new_spider(new_ver)
        local('mv slave_develop_new/workspace/spider/SpiderClient ./')
        file_name = '{0}_{1}_spider.tar.gz'.format(old_ver, new_ver)
        local('tar -zcvf {0} SpiderClient'.format(file_name))
        local('md5 {0}'.format(file_name))
    return path


def _deploy_spider():
    with cd('/search/test'):
        run('rm -rf slave_develop_new')
        put('{0}/spider_slave.tar.gz', './')


@roles('test_spider')
def _deploy_totest():
    _deploy_spider()


def deploy(path, role=None):
    rs = {
        "test_spider": _deploy_spider
    }
    execute(rs[role], args=(path,))


if __name__ == '__main__':
    # pull_source('http://gitlab.uc.online/spider_new/Spider.git', 'release_v1.0.0')
    # path = _build_dir()
    # path='build_2017-08-25-T21:04:46'
    # path = None
    # path = build('release_v1.0.2', 'release_v1.0.0')
    # deploy(path, 'test_spider')
    build('slave.20171220.a', 'Spider.20171221.a')
