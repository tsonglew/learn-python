import os.path
import random


# 导入tornado模块
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


# 定义http请求的端口
from tornado.options import define, options
define("port", default=8000, help="run on the given port", type=int)


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        # 使用RequestHandler类的render方法告诉tornado读入模板
        self.render('index.html')


class MungedPageHandler(tornado.web.RequestHandler):
    def map_by_first_letter(self, text):
        mapped = dict()
        for line in text.split('\r\n'):
            for word in [x for x in line.split(' ') if len(x) > 0]:
                if word[0] not in mapped: mapped[word[0]] = []
                mapped[word[0]].append(word)
        return mapped

    def post(self):
        source_text = self.get_argument('source')
        text_to_change = self.get_argument('change')
        source_map = self.map_by_first_letter(source_text)
        change_lines = text_to_change.split('\r\n')
        self.render('munged.html', source_map=source_map, change_lines=change_lines,
                choice=random.choice)


if __name__ == '__main__':
    # 使用tornado的options模块来解析命令行
    tornado.options.parse_command_line()
    # 创建Application类的实例
    app = tornado.web.Application(
            # handlers参数传递给Application,告诉tornado应用哪个类来响应请求
            handlers=[(r'/', IndexHandler), (r'/poem', MungedPageHandler)],
            # 传递static_path参数告诉tornado从特定位置提供静态文件
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            # 调用测试模块:tornado.autoreload
            debug=True
            )
    # Application对象被创建后传递给HTTPServer对象
    http_server = tornado.httpserver.HTTPServer(app)
    # 使用命令行指定的端口进行监听(通过options对象取出)
    http_server.listen(options.port)
    # 程序准备好接受HTTP请求后创建IOLoop的实例
    tornado.ioloop.IOLoop.instance().start()
