# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os.path


from tornado.options import options, define
define("port", default=8000, help="run on the given port", type=int)


# 定义Application子类
class Application(tornado.web.Application):
    def __init__(self):
        # 创建处理类列表
        handlers = [
                ('/', MainHandler)
                ]
        # 设置字典
        settings = dict(
                template_path=os.path.join(os.path.dirname(__file__), "templates"),
                static_path=os.path.join(os.path.dirname(__file__), "static"),
                debug=True
                )
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
                "index.html",
                page_title="Burt's Books | Home",
                header_text="Welcome to Burt's Books!"
                )


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
