import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


from tornado.options import options, define
define("port", default=8000, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
                "index.html",
                header_text = "Here goes the header",
                footer_text = "Here goes the footer"
                )


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
            headlers=[('/', MainHandler)]
            )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
