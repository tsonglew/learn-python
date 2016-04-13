# -*- coding: utf-8 -*-
# 可执行异步的HTTP请求
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient


import urllib
import json
import datetime
import time


from tornado.options import options, define
define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    # tornado默认在函数处理返回时关闭客户端的连接，处理一个需要回调函数的异步请求
    # 时需要连接保持开启状态直到回调函数执行完毕，@tornado.web.asynchronous装饰器
    # 告诉tornado保持连接开启
    @tornado.web.asynchronous
    def get(self):
        query = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()
        # AsyncHTTPClient的fetch方法不返回调用结果，而返回一个callback参数;指定
        # 的方法和函数在HTTP请求结束时被调用,并使用HTTPResponse作为其参数
        client.fetch("http://search.twitter.com/search.json?" + \
                urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}),
                # 指定on_response方法作为回调函数
                callback=self.on_response)

    def on_response(self, response):
        body = json.loads(response.body)
        result.count = len(body['results'])
        now = datetime.datetime.utcnow()
        raw_oldest_tweet_at = body['results'][-1]['created_at']
        oldest_tweet_at = datetime.datetime.striptime(raw_oldest_tweet_at,
                "%a, %d %b %Y %H:%M:%S +0000")
        seconds_diff = time.mktime(oldest_tweet_at.timetuple())
        tweets_per_second = float(result_count) / seconds_diff
        self.write("""
        <div style="text-align: center">
            <div style="font-size: 72px">%s</div>
            <div style="font-size: 144px">%.02f</div>
            <div style="font-size: 24px">tweets per second</div>
        </div>""" % (self.get_argument('q'), tweets_per_second))
        # 调用finish方法显示地告诉tornado关闭连接（否则请求将可能挂起）
        self.finish()


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(hanlers=[(r'/', IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
