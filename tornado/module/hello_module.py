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
        self.render("hello.html")


class HelloModule(tornado.web.UIModule):
    def render(self):
        return "<h1>Hello, world!</h1>"


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
            handlers=[('/', HelloHandler)],
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            # 把名为Hello的模块的引用和HelloModule类结合起来
            ui_modules={'Hello': HelloModule}
            )
    server = tornado.httpserver.HTTPServer(app)
    server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
