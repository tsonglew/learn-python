# recv_count.py
# Think of this function as receiving values rather than generating them

def recv_count():
    try:
        while True:
            n = (yield)
            print "T-minus", n
    except GeneratorExit:
        print "Kaboom!"

r = recv_count()
r.next() # r.send(None)
