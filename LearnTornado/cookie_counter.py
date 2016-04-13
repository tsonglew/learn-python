# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.options


from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        # 取得浏览器的cookies，以防浏览器中得恶意修改
        # tornado将cookie值编码为Base-64字符串，并添加时间戳和cookie内容的HMAC签名
        # 当cookie时间戳太久（或来自未来），签名和期望值不匹配，get_secure_cookie()
        # 将认为cookie已经被篡改
        cookie = self.get_secure_cookie("count")
        count = int(cookie) + 1 if cookie else 1

        countString = "1 time" if count == 1 else "%d times" % count

        # 发送浏览器的cookies，以防浏览器中得恶意修改
        self.set_secure_cookie("count", str(count))

        self.write(
                '<html><head><title>Cookie Counter</title></head>'
                '<body><h1>You’ve viewed this page %s.</h1>' % countString +
                '</body></html>'
                )


if __name__ == "__main__":
    tornado.options.parse_command_line()
    settings = {
            # Python shell下：
            # >>> import base64, uuid
            # >>> base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
            # 产生唯一的随即字符串
            "cookie_secret": "bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E="
            }
    application = tornado.web.Application([
        (r'/', MainHandler)
        ], **settings)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
