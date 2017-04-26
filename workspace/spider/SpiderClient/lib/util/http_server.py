#!/usr/bin/env python
# coding=UTF-8
'''
    Created on 2013-11-20
    @author: devin
    @desc:
        http server
'''
import sys
import socket
import SocketServer
import SimpleHTTPServer
import urlparse
from gevent.pywsgi import WSGIServer
from gevent import monkey

monkey.patch_all()

from gevent.pywsgi import WSGIServer


class URLParams:
    def __init__(self, params, path):
        self.params = params
        self.path = path

    def get(self, key):
        if key in self.params:
            print self.params[key][0]
            return self.params[key][0]
        return None

    def get_array(self, key):
        if key in self.params:
            return self.params[key]
        return []

    def get_json_obj(self, key):
        import jsonlib
        print self.params[key][0]
        if key in self.params:
            print jsonlib.read(self.params[key][0])
            return jsonlib.read(self.params[key][0])
        return None


class ThreadedHTTPRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    dispatchers = {}

    @classmethod
    def register(self, path, fun):
        self.dispatchers[path] = fun

    def do_GET(self):
        print  'herer', self.path
        o = urlparse.urlparse(self.path)
        print o.query
        params = urlparse.parse_qs(o.query)

        response = ''
        if o.path in self.dispatchers:
            fun = self.dispatchers[o.path]
            response = fun(URLParams(params, o.query))
        # send data
        self.send_response(200)
        self.end_headers()
        self.wfile.write(response)


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass


class HttpServer:
    '''
    def __init__(self, host, port):
        self.server = ThreadedTCPServer((host, port), ThreadedHTTPRequestHandler)

    def register(self, path, fun):
        ThreadedHTTPRequestHandler.register(path, fun)

    def run(self):
        self.server.serve_forever() 
    '''

    def __init__(self, host, port):
        self.path = {}
        self.server = WSGIServer((host, port), self.application)

    def register(self, path, fun):
        self.path[path] = fun

    def application(self, environ, start_response):
        status = '200 OK'

        headers = [
            ('Content-Type', 'text/html')
        ]

        path_info = environ['PATH_INFO']
        osquery = environ['QUERY_STRING']
        response = 'lao niang kan ni shi bu shi timeout !'

        if path_info in self.path:
            params = urlparse.parse_qs(osquery)

            p = URLParams(params, osquery)
            p.remote_addr = environ['REMOTE_ADDR']
            response = self.path[path_info](p)

        start_response(status, headers)
        return response

    def run(self):
        self.server.serve_forever()


def Test(params):
    # return "Test:" + str(params)
    return 'ni hao a'
    return params.get("source")


if __name__ == "__main__":
    HOST, PORT = "10.10.234.24", 8086
    server = HttpServer(HOST, PORT)
    server.register("/test", Test)
    server.run()
