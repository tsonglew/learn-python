# -*- coding: utf-8 -*-


from collections import deque


class linehistory:
    def __init__(self, lines, histlen=3):
        self.lines = lines
        # deque: elements could be appended or removed from both sides
        self.history = deque(maxlen=histlen)

    def __iter__(self):
        # The second argument should be the start index
        for lineno, line in enumerate(self.lines, 1):
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()
