# -*- coding: utf-8 -*-


CHUNKSIZE = 8192

def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)

def reader2(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        pass
