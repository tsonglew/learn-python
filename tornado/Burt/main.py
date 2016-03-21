# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import os.path


from tornado.options import options, define
define("port", default=8000, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
                "index.html",
                page_title="Burt's Books | Home",
                header_text="Welcome to Burt's Books!"
                )


class RecommendedHandler(tornado.web.RequestHandler):
    def get(self):
        self.render(
                "recommended.html",
                page_title="Burt's Books | Recommended Reading",
                header_text="Recommeded Reading",
                books=[
                    {
                        "title": "Programming",
                        "subtitle": "Building",
                        "image": "/static/images/1.gif",
                        "author": "Toby",
                        "date_added": 131,
                        "date_released": "August 2007",
                        "isbn": "978-0-596",
                        "description": "<p>This fascinationg book </p>"
                    }
                ]
        )


class BookModule(tornado.web.UIModule):
    def render(self, book):
        return self.render_string(
                'modules/book.html',
                book=book
        )

    def embedded_javascript(self):
        return "document.write(\"hi!\")"


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(
            handlers=[(r'/', MainHandler),
                (r'/recommended/', RecommendedHandler)
            ],
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            ui_modules={'Book': BookModule}
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
