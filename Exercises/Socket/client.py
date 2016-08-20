#!/usr/bin/env python
#-*- coding: utf-8 -*-


import socket
import sys


# Address Family:
#     AF_INET(IPv4网络协议的套接字类型)-->用于Internet进程间通信
#     AF_UNIX --> 用于同一台机器进程间通信
# Type(套接字类型):
#     STREAM socket (流式套接字, 主要用于TCP)
#     SOCKET_DGRAM (数据报套接字, 主要用于UDP协议)

# 创建socket
# socket.socket创建一个socket，返回该socket的描述符
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print('Failed to create socket. Error code: {a}, Error message: {b}'.format(a=str(msg[0]), b=msg[1]))
    # 引发SystemExit异常, Python解释器直接退出
    sys.exit()

print('Socket Created!')


# 函数socket.gethostbyname获取远程主机的IP地址
host = 'www.google.com'
port = 80

try:
    remote_ip = socket.gethostbyname(host)

except socket.gaierror:
    print('Hostname could not be resolved. Exiting')
    sys.exit()

print('Ip address of {h} is {r}'.format(h=host, r=remote_ip))


# 连接远程服务器
s.connect((remote_ip, port))

print('Socket Connected to {h} on ip {r}'.format(h=host, r=remote_ip))


# 发送数据
message = "GET / HTTP/1.1\r\n\r\n"

try:
    s.sendall(message)
except socket.error:
    print('Send failed')
    sys.exit()

print('Message send successfully')


# 接收数据(recv函数)
reply = s.recv(4096)

print(reply)


# 关闭socket
s.close()
