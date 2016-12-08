#-*- coding: utf-8 -*-

# 归并排序(Merge sort)
#
# 原理:
#
# 迭代法
# 申请空间，使其大小为两个已经排序序列之和，该空间用来存放合并后的序列
# 设定两个指针，最初位置分别为两个已经排序序列的起始位置
# 比较两个指针所指向的元素，选择相对小的元素放入到合并空间，并移动指针到下一位置
# 重复步骤3直到某一指针到达序列尾
# 将另一序列剩下的所有元素直接复制到合并序列尾

# 递归法
# 假设序列共有n个元素：
# 将序列每相邻两个数字进行归并操作，形成n/2个序列，排序后每个序列包含两个元素
# 将上述序列再次归并，形成n/4个序列，每个序列包含四个元素
# 重复步骤2，直到所有元素排序完毕

# 时间复杂度:
#     最优: O(n)
#     最差: O(nlogn)
def merge_sort(alist):
    if len(alist) <= 1:
        return alist
    middle = len(alist)//2
    left = merge_sort(alist[:middle])
    right = merge_sort(alist[middle:])
    print left + right
    return merge(left, right)

def merge(left, right):
    l, r = 0, 0
    result = []
    while l<len(left) and r<len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    return result+left[l:]+right[r:]

if __name__ == '__main__':
    result = merge_sort(['Q', 'H', 'C', 'Y', 'P', 'A', 'M', 'S', 'R', 'D', 'F', 'X'])
    print 'result: ',
    print result
