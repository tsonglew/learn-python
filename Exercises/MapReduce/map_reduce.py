# -*- coding: utf-8 -*-

import collections
import itertools
import multiprocessing


class MapReduce(object):
    def __init__(self, map_func, reduce_func, num_workers=None):
        self.map_func = map_func
        self.reduce_func = reduce_func
        self.pool = multiprocessing.Pool(num_workers)

    def partition(self, mapped_values):
        partitioned_data = collections.defaultdict(list)
        for key, value in mapped_values:
            partitioned_data[key].append(value)
        return partitioned_data.items()

    def __call__(self, inputs, chunksize=1):
        map_responses = self.pool.map(
                self.map_func, inputs, chunksize=chunksize
                )
        # Return a chain object whose .next() method returns elements from the
        # first iterable until it is exhuasted, then elements from the next
        # iterable, until all of the iterables are exhuasted
        partitioned_data = self.partition(itertools.chain(*map_responses))

        reduced_values = self.pool.map(self.reduce_func, partitioned_data)
        return reduced_values
