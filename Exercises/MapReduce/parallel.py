# -*- coding: utf-8 -*-

import os
import time
import multiprocessing # Process based "threading" interface


def task(args):
    time.sleep(1)
    pid = os.getpid() # Return current process
    return pid, args

start = time.time()
# Returns a process pool object, processes is the number of worker processes
# to use.
pool = multiprocessing.Pool(processes=4)
result = pool.map(task, range(10))
print result
print "Cost: {}".format(time.time() - start)
