#-*- coding: utf-8 -*-

# 选择排序(selection sort)
# 原理:
# 1. 在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，
# 2. 再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。
# 3. 重复第二步，直到所有元素均排序完毕。


# 时间复杂度:
#     最差: O(n^2)
#     最优: O(n^2)


def selection_sort(alist):
    length = len(alist)
    for index in range(length):
        m = index
        for i in range(index, length):
            if alist[i] < alist[m]:
                m = i
        alist[m], alist[index] = alist[index], alist[m]
    return alist
