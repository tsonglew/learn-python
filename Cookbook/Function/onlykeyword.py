# -*- coding: utf-8 -*-


def recv(maxsize, *, block):
    """Receive a message"""
    pass

recv(1024, block=True)

def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m

minimum(1, 5, 2, -5, 10)
minimum(1, 5, 2, -5, 10, clip=0)

