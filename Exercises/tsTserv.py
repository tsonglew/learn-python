#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 模块导入
from socket import *
from time import ctime


HOST = ''  # 变量为空，表示bind()函数可以绑定在所有有效的地址上
PORT = 21567  # 设置端口号
BUFSIZ = 1024  # 设置缓冲区
ADDR = (HOST, PORT)


tcpSerSock = socket(AF_INET, SOCK_STREAM)  # 创建TCP/IP套接字
tcpSerSock.bind(ADDR)  # 绑定地址到套接字
tcpSerSock.listen(5)  # 开始监听，最多允许5个连接同时连入


while True:
    print 'waiting for connection...'
    tcpCliSock, addr = tcpSerSock.accept() #被动接受TCP客户端连接，等待连接的到来
    print '...connected from:', addr

# 有连接时进入对话循环
    while True:
        data = tcpCliSock.recv(BUFSIZ)  # 用户发送数据
        # 消息为空表示客户端已经退出
        if not data:
            break
        tcpCliSock.send('[%s] %s' % (ctime(), data))

        tcpCliSock.close()


tcpSerSock.close()
