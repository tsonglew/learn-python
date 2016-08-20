#!/usr/bin/env python
#-*- coding: utf-8 -*-


CONNECTION_LIST = []

read_sockets, write_sockets, error_sockets = select.select(CONNECTION_LIST, [], [])

def broadcast_data(sock, message):
    # Do not send the message to master socket and the client who has send us
    # the message
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock:
            try:
                socket.send(message)
            except:
                # Broken socket connection
                socket.close()
                CONNECTION_LIST.remove(socket)
