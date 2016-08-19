#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
from tornado.httpserver import HTTPServer
from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop



class TestHandler(RequestHandler):
    def get(self):
        import pdb
        pdb.set_trace()
        self.write("Hello, World!\n")


#class TestHandler(RequestHandler):
#    def get(self):
#        self.write("Hello, World!\n")

settings = {
    "static_path" : os.path.join(os.path.dirname(__file__), "static"),
}

application = Application([
    (r"/", TestHandler),
], **settings)

if __name__ == "__main__":
    server = HTTPServer(application)
    server.listen(8000)
    IOLoop.instance().start()
