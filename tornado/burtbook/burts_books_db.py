# -*- coding: utf-8 -*-
import os.path
import tornado.locale
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo


from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
                (r"/", MainHandler),
                (r"/recommended/", RecommendedHandler),
                # 根据书籍的ISBN渲染一个已存在书籍的表单
                (r"/edit/([0-9Xx\-]+)", BookEditHandler),
                # 不存在信息的编辑表单
                (r"/add", BookEditHandler)
        ]
        settings = dict(
                tempalte_path=os.path.join(os.path.dirname(__file__), "templates"),
                static_path=os.path.join(os.path.dirname(__file__), "static"),
                ui_modules={"Book": BookModule},
                debug=True
        )
        conn = pymongo.MongoClient("localhost", 27017)
        # 添加db属性来连接MongoDB服务器
        self.db = conn["bookstore"]
        tornado.web.Application.__init__(self, handlers, **settings)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html",
                page_title = "Burt's Books | Home",
                header_text = "Welcome to Burt's Books!",
        )


class RecommendedHandler(tornado.web.RequestHandler):
    def get(self):
        coll = self.application.db.books
        # 使用连接的find方法从数据库取得书籍文档的列表
        books = coll.find()
        # 将列表传递给RecommendedHandler的get方法
        self.render(
                "recommended.html",
                page_title = "Burt's Books | Recommended Reading",
                header_text = "Recommended Reading",
                books = books
        )



class BookEditHandler(tornado.web.RequestHandler):
    # 渲染一个显示已存在书籍数据的HTML表单
    def get(self, isbn=None):
        book = dict()
        if isbn:
            coll = self.application.db.books
            book = coll.find_one({"isbn": isbn})
        self.render("book_edit.html",
                page_title="Burt's Books",
                header_text="Edit Book",
                book=book)

    # 从表单中取得数据,更新书籍记录或添加新的书籍
    def post(self, isbn=None):
        import time
        book_fields = ['isbn', 'title', 'subtitle', 'image', 'author',
                'date_released', 'description']
        coll = self.application.db.books
        book = dict()

        if isbn:
            book = coll.find_one({"isbn": isbn})
        for key in book_fields:
            book[key] = self.get_argument(key, None)

        if isbn:
            coll.save(book)
        else:
            book['date_added'] = int(time.time())
            coll.insert(book)
        self.redirect("/recomended/")


class BookModule(tornado.web.UIModule):
    def render(self):
        return self.render_string(
                "module/books.html",
                book=book,
        )

    def css_files(self):
        return "/static/css/recommended.css"

    def javascript_files(self):
        return "/static/js/recommended.js"


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
