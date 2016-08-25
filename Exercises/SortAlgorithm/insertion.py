#-*- coding: utf-8 -*-

# 插入排序(insertion sort)
# 原理:
# 1. 从第一个元素开始，该元素可以认为已经被排序
# 2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
# 3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
# 4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
# 5. 将新元素插入到该位置后
# 6. 重复步骤2~5

# 时间复杂度:
#     最差: O(n^2)
#     最优: O(n)


def insertion_sort(alist):
    length = len(alist)
    if length == 1:
        return alist
    b = insertion_sort(alist[1:])
    lengthb = len(b)
    for index in range(lengthb):
        if alist[0] <= b[index]:
            return b[:index] + [alist[0]] + b[index:]
    return b + [alist[0]]
