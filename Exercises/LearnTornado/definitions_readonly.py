# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import pymongo


from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [(r"/(\w+)", WordHandler)]
        conn = pymongo.MongoClient("localhost", 27017)
        # 在Application对象中添加db属性,以在任何RequestHandler对象中使用self.application.db访问
        self.db = conn["example"]
        tornado.web.Application.__init__(self, handlers, debug=True)


class WordHandler(tornado.web.RequestHandler):
    def get(self, word):
        #  将集合对象指定给变量coll
        coll = self.application.db.words
        word_doc = coll.find_one({"word": word})
        if word_doc:
            # 删除_id键(以便Python的json库将其序列化)
            del word_doc["_id"]
            # write方法自动序列化字典为JSON格式
            self.write(word_doc)
        else:
            self.set_status(404)
            self.write({"errror": "word not found"})


if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
