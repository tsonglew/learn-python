#-*- coding: utf-8 -*-
# 模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。

class My_Singleton(object):
    def foo(self):
        pass

my_singleton = My_Singleton()
