#!/usr/bin/env python
#-*- coding: utf-8 -*-

import socket
import sys

HOST = ''
PORT = 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print('Bind failed. Error Code: {m1} Message {m2}'.format(m1=str(msg[0]), m2=msg[1]))
    sys.exit()
print('Socket bind completed')

s.listen(10)
print('Socket now listening')

while 1:
    conn, addr = s.accept()
    print('Connected with {a1} : {a2}'.format(a1=addr[0], a2=str(addr[1])))
    data = conn.recv(1024)
    reply = 'OK...' + data
    if not data:
        break
    conn.sendall(reply)

conn.close()
s.close()
