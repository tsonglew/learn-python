#!/usr/bin/env python
#-*- coding: utf-8 -*-


import socket
import sys


# 绑定socket
HOST = '' # 所有可用接口
PORT = 8888 # 任意端口

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print('Bind failed. Error Code: {m1} Message: {m2}'.format(m1=str(msg[0]), m2=msg[1]))
    sys.exit()
print('Socket bind complete')


# 监听连接
s.listen(10) # 参数(backlog)控制连接个数
print('Socket now listening')


# 接收连接
conn, addr = s.accept()
print('Connected with {a}: {ad}'.format(a=addr[0], ad=str(addr[1])))


data = conn.recv(1024)
conn.sendall(data)

conn.close()
s.close()
