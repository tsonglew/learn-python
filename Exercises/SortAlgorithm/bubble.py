#-*- coding: utf-8 -*-

# 冒泡排序(bubble sort)
# 原理:
# 1. 比较相邻的元素。如果第一个比第二个大，就交换他们两个。
# 2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对。这步做完后，最后的元素会是最大的数。
# 3. 针对所有的元素重复以上的步骤，除了最后一个。
# 4. 持续每次对越来越少的元素重复上面的步骤，直到没有任何一对数字需要比较。

# 时间复杂度:
#     最差: O(n^2)
#     最优: O(n)


def bubble_sort(alist):
    length = len(alist)
    for index in range(length-1):
        for i in range(0, length-index-1):
            if alist[i] > alist[i+1]:
                alist[i+1], alist[i] = alist[i], alist[i+1]
    return alist


# 优化: 添加标记，在排序完成时停止排序

def bubble_sort_flag(alist):
    length = len(alist)
    for index in range(length):
        flag = True
        for i in range(0, length-index-1):
            if alist[i] > alist[i+1]:
                alist[i+1], alist[i] = alist[i], alist[i+1]
                flag = False
        if flag:
            return alist
    return alist
