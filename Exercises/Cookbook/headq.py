import heapq

class PriorityQueue:
    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        # priority with minus sign in order to sort the elements from the
        # larger one to the smaller one
        # with an tuple of the three elements, the instances could be compared
        # without any errors turning up
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]
