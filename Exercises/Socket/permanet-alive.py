#!/usr/bin/env python
#-*- coding: utf-8 -*-


import sys
import socket
from thread import start_new_thread

HOST = ''
PORT = 8888

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

try:
    s.bind((HOST, PORT))
except socket.error, msg:
    print('Bind failed. Error code: {m1} Message {m2}'.format(m1=str(msg[0]), m2=msg[1]))
    sys.exit()
print('Socket bind complete')

s.listen(10)
print('Socket now listening')


def clientthread(conn):
    conn.send('Welcome to the server. Type something and hit entern')

    while True:
        data = conn.recv(1024)
        reply = ''.join(['OK..', data])
        if not data:
            break
        conn.sendall(reply)
    conn.close()

while True:
    conn, addr = s.accept()
    print('Conncted with {a1}:{a2}'.format(a1=addr[0], a2=str(addr[1])))
    start_new_thread(clientthread, (conn,))

s.close()
