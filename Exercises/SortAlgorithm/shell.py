#-*- coding: utf-8 -*-

# 希尔排序/递减增量排序算法
# 原理:
# 基于插入排序的性质:
# * 插入排序在对几乎已经排好序的数据操作时，效率高，即可以达到线性排序的效率
# * 但插入排序一般来说是低效的，因为插入排序每次只能将数据移动一位。
#
# *希尔排序* 通过将比较的全部元素分为几个区域来提升插入排序的性能。这样可以让一
# 个元素可以一次性地朝最终位置前进一大步(每次以一定步长以一定步长进行排序，直至
# 步长为1)。然后算法再取越来越小的步长进行排序,算法的最后一步就是普通的插入排序
#
# 步长选择:
# 只要最终步长为1都可以正常工作，Donald Shell最初建议步长选择为n/2并且对步长取
# 半直到步长达到1。另外步长还可以使用Sedgewick提出的(1, 5, 19, 41, 109,…)。
# 也可以使用斐波那契数列除去0和1将剩余的数以黄金分区比的两倍的幂进行运算得到的数列。

# 时间复杂度:
#     最差: O(nlog(2)n)
#     最优: O(n)


def shell_sort(alist):
    length = len(alist)
    gap = length / 2
    while gap > 0:
        for i in range(gap, length):
            temp = alist[i]
            j = i
            # 插入排序
            while j >= gap and alist[j-gap] > temp:
                alist[j] = alist[j-gap]
                j -= gap
            alist[j] = temp
        gap = gap / 2
    return alist
