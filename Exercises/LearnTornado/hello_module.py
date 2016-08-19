# -*- coding: utf-8 -*-
import tornado.web
import tornado.ioloop
import tornado.options
import tornado.httpserver
import os.path


from tornado.options import options, define
define("port", default=8000, help="run on the given port", type=int)


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('hello.html')


class HelloModule(tornado.web.UIModule):
