import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
import tornado.httpclient
import tornado.gen


import urllib
import json
import datetime
import time


from tornado.options import options, define
define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    @tornado.gen.engine
    def ger(self):
        query = self.get_argument('q')
        client = tornado.httpclient.AsyncHTTPClient()
        # yield关键字以及tornado.gen.Task对象的一个实例实现函数的调用和参数的传入
        # yield的使用返回程序对Tornado的控制，允许在HTTP请求进行中执行其他任务。
        # HTTP请求完成时，RequestHandler方法在其停止的地方恢复。
        response = yield tornado.gen.Task(client.fetch,
                "http://search.twitter.com/search.json?" + \
                        urllib.urlencode({"q": query, "result_type": "recent", "rpp": 100}))
        body = json.loads(response.body)
        result_count = len(body['results'])
        now = datetime.datetime.utcnow()
        raw_oldest_tweet_at = body['results'][-1]['created_at']
        oldest_tweet_at = datetime.datetime.strptime(raw_oldest_tweet_at,
                "%a, %d %b %Y %H:%M:%S +0000")
        seconds_diff = time.mktime(now.timetuple()) - \
                time.mktime(oldest_tweet_at.timetuple())
        tweets_per_second = float(result_count) / seconds_diff
        self.write("""
        <div style="text-align: center">
            <div style="font-size: 72px">%s</div>
            <div style="font-size: 144px">%.02f</div>
            <div style="font-size: 24px">tweets per second</div>
        </div>""" % (query, tweets_per_second))
        self.finish()


if __name__ == "__main__":
    tornado.options.parse_command_line()
    app = tornado.web.Application(handlers=[(r"/", IndexHandler)])
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()
