import os

f = open("ex.txt", mode="rb", buffering=0)
pid = os.fork()
print("getpid {:>5}, fork {:>5}, fd {}: {}".format(os.getpid(), pid, f.fileno(), f.read(6)))
f.close()
