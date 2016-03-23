# -*- coding: utf-8 -*-
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient


import urllib
import json
import datetime
import time


from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 从查询参数中抓取参数q
        query = self.get_argument('q')
        # 用q执行一个到twitter搜索API的请求
        # 实例化一个Tornado的HTTPClient类
        client = tornado.httpclient.HTTPClient()
        # 调用fetch方法(使用要获取的url作参数),返回一个HTTPResponse对象,body包含获取的任何数据(json格式)
        response = client.fetch("http://search.twitter.com/search.json?" + \
                # 将url中的键值对以链接符&划分
                urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}))
        # 使用json模块来从结果中创建一个数据结构
        body = json.loads(response.body)
        result_count = len(body['results'])
        now = datetime.datetime.utcnow()
        raw_oldest_tweet_at = body['results'][-1]['created_at']
        oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,
                "%a, %d %b %y %H:%M:%S +0000")
        seconds_diff = time.mktime(now.timetuple())
        tweets_per_second = float(result_count) / seconds_diff
        self.write("""
        <div style="text-align: center">
            <div style="font-size: 72px">%s</div>
            <div style="font-size: 144px">%.02f</div>
            <div style="font-size: 24px">tweets per second</div>
        </div>"""% (query, tweets_per_second))


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
