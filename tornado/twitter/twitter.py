# -*- coding: utf-8 -*-
import tornado.web
import tornado.httpserver
import tornado.auth
import tornado.ioloop


# TwitterMixin类提供Twitter功能
class TwitterHandler(tornado.web.RequestHandler, tornado.auth.TwitterMixin):
    @tornado.web.asynchronous
    def get(self):
        oAuthToken = self.get_secure_cookie('oauth_token')
        oAuthSecret = self.get_secure_cookie('oauth_secret')
        userID = self.get_secure_cookie('user_id')

        # 检查请求是否包括一个oauth_token查询字符串参数，若有，则把这个请求看作
        # 是一个来自Twitter验证过程的回调
        if self.get_argument('oauth_token', None):
            # get_authenticated方法把临时令牌换为用户的访问令牌，当到Twitter的API
            # 请求返回时，执行回调函数self._twitter_on_auth方法
            self.get_authenticated_user(self.async_callback(self._twitter_on_auth))
            return

        # oauth_token参数没有被发现，寻找应用在Twitter给定一个合法用户时设置的access_key
        # 和access_secret cookies
        elif oAuthToken and oAuthSecret:
            # 用key和secret组装访问令牌
            accessToken = {
                    'key': oAuthToken,
                    'secret': oAuthSecret
                    }
            # 向Twitter API的/users/show发出请求
            self.twitter_request('/users/show',
                    # access_token应该是一个字典，包括用户的OAuth访问令牌的key键
                    # 和用户OAuth secret的secret键
                    access_token=accessToken,
                    user_id=userID,
                    callback=self.async_callback(self._twitter_on_user)
                    )
            return

        # 重定向到Twitter的验证页面
        self.authorize_redirect()

    def _twitter_on_auth(self, user):
        if not user:
            self.clear_all_cookies()
            raise tornado.web.HTTPError(500, 'Twitter authentication failded')

        # 设置应有的cookies
        self.set_secure_cookie('user_id', str(user['id']))
        self.set_secure_cookie('oauth_token', user['access_token']['key'])
        self.set_secure_cookie('oauth_secret', user['access_token']['secret'])

        self.redirect('/')

    def _twitter_on_user(self, user):
        if not user:
            # 清除为应用用户储存的cookies
            self.clear_all_cookies()
            raise tornado.web.HTTPError(500, "Couldn't retrieve user imformation")

        self.render('home.html', user=user)


class LogoutHandler(tornado.web.RequestHandler):
    def get(self):
        self.clear_all_cookies()
        self.render('logout.html')


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
                (r'/', TwitterHandler),
                (r'/logout', LogoutHandler)
                ]

        settings = {
                # Twitter应用详细设置页面中列出的值
                'twitter_consumer_key': 'twitter_consumer_key',
                'twitter_consumer_secret': 'twitter_consumer_secret',
                'cookie_secret': 'NTliOTY5NzJkYTVlMTU0OTAwMTdlNjgzMTA5M2U3OGQ5NDIxZmU3Mg==',
                'template_path': 'templates',
                }

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
