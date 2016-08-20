#!/usr/bin/env python
#-*- coding: utf-8 -*-
import sys
import socket
import select
import string


def prompt():
    sys.stdout.write('<You> ')
    sys.stdout.flush()


if __name__ == '__main__':
    # 获取host, port
    if len(sys.argv) < 3:
        print('Usage: python telnet.py hostname port')
        sys.exit()
    host = sys.argv[1]
    port = int(sys.argv[2])

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置阻塞模式下socket的超时时间
    s.settimeout(2)

    try:
        s.connect((host, port))
    except:
        print('Unable to connect')
        sys.exit()
    print('Connected to remote host. Start sending message')
    prompt()

    while True:
        socket_list = [sys.stdin, s]

        read_sockets, write_sockets, error_sockets = select.select(socket_list, [], [])

        for sock in read_sockets:
            # 从服务器获取数据
            if sock == s:
                data = sock.recv(4096)
                if not data:
                    print('\nDisconnected from chat server')
                    sys.exit()
                else:
                    sys.stdout.write(data)
                    prompt()

            # 用户输入数据
            else:
                msg = sys.stdin.readline()
                s.send(msg)
                prompt()
