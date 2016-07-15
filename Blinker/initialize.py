# init with signal()
from blinker import signal
initialized = signal("initialized")
# for each time signal() returns a signal object

# subscribe signal
def subscriber(sender):
    print "Got a signal sent by %r " % sender

ready = signal('ready')
# signal.connect() register a function and allocate it when the signal is
# triggered
ready.connect(subscriber)

class Processor:
    def __init__(self, name):
        self.name = name

    def go(self):
        ready = signal('ready')
        # trigger the ready signal, self as the parameter because Processor
        # instance is the sender of the signal
        ready.send(self)
        print "Processing."
        # this signal won't be subscribed but could be sent
        complete = signal('complete')
        complete.send(self)

    def __repr__(self):
        return '<Processor %s>' % self.name

processor_a = Processor('a')
processor_a.go()


def b_subscriber(sender):
    print "Caught signal from processor_b."
    assert sender.name == 'b'

processor_b = Processor('b')
ready.connect(b_subscriber, sender=processor_b)

processor_a.go()
processor_b.go()


# extra key words could be sent by send() to the subscribers
send_data = signal('send-data')
@send_data.connect
def receive_data(sender, **kw):
    print "Caught signal from %r, data %r" % (sender, kw)
    return 'received!'

result = send_data.send('anonymous', abc=123)
# send() collects each subscribers' return value and form a list


# Anonymous Signal
from blinker import Signal
class AltProcessor:
    # the following are two different signals
    on_ready = Signal()
    on_complete = Signal()

    def __init__(self, name):
        self.name = name

    def go(self):
        self.on_ready.send(self)
        print "Alternate processing."
        self.on_complete.send(self)

    def __repr__(self):
        return '<AltProcessor %s>' % self.name

