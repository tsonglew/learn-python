#-*- coding: utf-8 -*-

# 快速排序
# 原理:
# 1. 从数列中挑出一个元素，称为"基准"（pivot），
# 2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
# 3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。

# 时间复杂度:
#     最差: O(n^2)
#     平均: O(nlogn)
#     最优: O(nlogn)

def Partition(r, low, high):
    pivot = r[low]
    while low < high:
        while low < high and r[high] >= pivot:
            high -= 1
        if low < high:
            r[low] = r[high]
            low += 1
        while low < high and r[low] <= pivot:
            low += 1
        if low < high:
            r[high] = r[low]
            high -= 1
    r[low] = pivot
    return low

def QuickSort(r, low, high):
    if low < high:
        pivotkey = Partition(r, low, high)
        QuickSort(r, low, pivotkey-1)
        QuickSort(r, pivotkey+1, high)

r = [3, 4, 2, 1, 10, 9, 0, 7, 2]
print('Before Sort: ', r)
QuickSort(r, 0, len(r)-1)
print('After Sort: ', r)
