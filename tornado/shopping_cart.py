import tornado.web
import tornado.httpserver
import tornado.ioloop
import tornado.options
from uuid import uuid4


# 维护库存中商品的数量，把商品加入购物车的购物者列表
class ShoppingCart(object):
    totalInventory = 10
    callbacks = []
    carts = {}

    def register(self, callback):
        self.callbacks.append(callback)

    def moveItemToCart(self, session):
        if session in self.carts:
            return
        self.carts[session] = True
        self.notifyCallbacks()

    def removeItemFromCart(self, session):
        if session not in self.carts:
            return
        del(self.carts[session])
        self.notifyCallbacks()

    # 已注册的回调函数被以当前可用库存数量调用，回调函数列表被清空以确保回调函数
    # 不会在一个已经关闭的连接上调用
    def notifyCallbacks(self):
        for c in self.callbacks:
            self.callbackHelper(c)
        self.callbacks = []

    def callbackHelper(self, callback):
        callback(self.getInventoryCount())

    def getInventoryCount(self):
        return self.totalInventory - len(self.carts)


# 每次请求时提供库存数量，并向浏览器渲染HTML模板
class DetailHandler(tornado.web.RequestHandler):
    def get(self):
        session = uuid4()
        count = self.application.shoppingCart.getInventoryCount()
        self.render("index.html", session=session, count=count)


# 提供操作购物车的接口
class CartHandler(tornado.web.RequestHandler):
    def post(self):
        action = self.get_argument('action')
        session = self.get_argument('session')

        if not session:
            self.set_status(400)
            return
        if action == 'add':
            self.application.shoppingCart.moveItemToCart(session)
        elif action == 'remove':
            self.application.shoppingCart.removeItemFromCart(session)
        else:
            self.set_status(400)


# 查询全局库存变化通知
class StatusHandler(tornado.web.RequestHandler):
    # 使tornado在get方法返回时不会关闭连接
    @tornado.web.asynchronous
    def get(self):
        # 使用self.async_callback包住回调函数确保回调函数中引发的异常不会使RequestHandler关闭连接
        self.application.shoppingCart.register(self.async_callback(self.on_message))

    def on_message(self, count):
        self.write('{"inventoryCount":"%d"}' % count)
        self.finish()


class Application(tornado.web.Application):
    def __init__(self):
        self.shoppingCart = ShoppingCart()

        handlers = [
                (r'/', DetailHandler),
                (r'/cart', CartHandler),
                (r'/cart/status', StatusHandler)
                ]

        settings = {
                'template_path': 'templates',
                'static_path': 'static'
                }

        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == "__main__":
    tornado.options.parse_command_line()

    app = Application()
    server = tornado.httpserver.HTTPServer(app)
    server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()
