#-*- coding: utf-8 -*-

# 堆排序
# 原理:
# 在堆的資料結構中，堆中的最大值總是位於根節點(在优先队列中使用堆的话堆中的最小值位于根节点)。堆中定義以下幾種操作：
# 最大堆調整（Max_Heapify）：將堆的末端子節點作調整，使得子節點永遠小於父節點
# 建立最大堆（Build_Max_Heap）：將堆所有數據重新排序
# 堆排序（HeapSort）：移除位在第一個數據的根節點，並做最大堆調整的遞迴運算

# 时间复杂度:
#     最差: O(nlog(2)n)
#     最优: O(nlog(2)n)
#     平均: O(nlog(2)n)
# 空间复杂度:
#     辅助: O(1)

def swap(array, a, b):
    """Swap two numbers in an array"""
    temp = array[a]
    array[a] = array[b]
    array[b] = temp

def sift_down(array, last_index):
    """sift biggest number down to the tail of an array"""
    index = 0
    while True:
        left_index = 2*index + 1
        right_index = 2*index + 2
        if left_index > last_index:
            break
        else:
            if right_index > last_index:
                next_index = left_index
            else:
                if array[left_index] >= array[right_index]:
                    next_index = left_index
                else:
                    next_index = right_index
        if array[next_index] <= array[index]:
            break
        temp = array[index]
        array[index] = array[next_index]
        array[next_index] = temp
        index = next_index
        print("next_index: ", next_index)

def heap_sort(array, length):
    """heap sort main function"""
    last_node = (length - 2) / 2
    for i in range(last_node, 0, -1):
        sift_down(array, length-1)

    for i in range(length-1, 1, -1):
        swap(array, 0, i)
        sift_down(array, i-1)
    swap(array, 0, 1)

if __name__ == '__main__':
    arr = [2, 4, 8, 3, 1, 9, 5]
    print("Before sort: ", arr)
    heap_sort(arr, len(arr))
    print("After sort: ", arr)
