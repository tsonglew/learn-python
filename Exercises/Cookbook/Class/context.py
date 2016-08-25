#-*- coding: utf-8 -*-
# 使对象支持上下文管理协议(with语句)

from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError('Already connected')
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


from functools import partial

conn = LazyConnection(('www.python.org', 80))

with conn as s:
    s.send(b'GET /index.html HTTP/1.0\r\n')
    s.send(b'Host: www.python.org\r\n')
    s.send(b'\r\n')
    resp = b''.join(iter(partial(s.recv, 8192), b''))

# 当出现with语句的时候，对象的__enter__()方法被触发，返回值被赋值给as声明的变量
# 然后with语句块里面的代码开始执行。最后，__exit__()方法被触发进行清理工作
# __exit__()的参数中exc_type, exc_value(参数必须为3个),
# traceback用于描述异常。如果程序正常结束，三个参数都为None。


# with语句嵌套使用连接
class LazyConnection2:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()


from functools import partial

conn = LazyConnection2(('www.python.org', 80))
with conn as s1:
    pass
    with conn as s1:
        pass

# LazyConnection类可以被看作一个连接工厂。一个列表被用来构建一个栈，每次__enter__()
# 方法执行的时候，他复制创建一个新的连接并将其加入到栈里面。__exit__()方法从栈中弹
# 出最后一个连接并关闭它。
