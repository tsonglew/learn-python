import threading

counter = 0

def worker():
    global counter
    counter += 1
    print("The Count is %d" % counter)
    print("----------------")

print("Starting up")
for i in range(10):
    threading.Thread(target=worker).start()
print("Finishing up")
