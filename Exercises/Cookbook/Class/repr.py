#-*- coding: utf-8 -*-


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        # 0指的是self本身
        return 'Pair({0.x!r}, {0.y!r})'.format(self)

    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)

# !r 格式化代码指明输出使用__repr__()代替默认的__str__()
# 自定义__repr__()和__str__()写详细的说明,如果__str__()未被定义就会使用__repr__()
# 来代替输出
