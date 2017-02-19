from types import coroutine

@coroutine
def read_await(sock):
    yield 'read_await', sock

@coroutine
def write_await(sock):
    yield 'write_await', sock

class Loop:
    async def sock_recv(self, sock, maxbytes):
        await read_wait(sock)
        return sock.recv(maxbytes)

    async def sock_accept(self, sock):
        await read_wait(sock)
        return sock.accept()

    async def sock_sendall(self, sock, data):
        while data:
            await write_wait(sock)
            nsent = sock.send(data)
            data = data[nsent:]
