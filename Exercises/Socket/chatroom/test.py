#!/usr/bin/env python
#-*- coding: utf-8 -*-


import socket
import select


sock1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


sock1.connect(('192.168.1.1', 25))
sock2.connect(('192.168.1.1', 25))


while True:
    # select的三个参数都是list类型, 分别代表读事件, 写事件, 错误事件,
    # 返回满足的事件
    rlist, wlist, elist = select.select([sock1, sock2], [], [], 5)
    if [rlist, wlist, elist] == [[], [], []]:
        print('Five seconds elapsed.\n')
    else:
        for sock in rlist:
            print(sock.recv(100))
