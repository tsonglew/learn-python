def comb_sort(alist):
    shrink = 1.3
    gap = len(alist)

    while True:
        gap = int(gap / shrink)
        i = 0
        if gap < 1:
            break
        else:
            while i + gap < length:
                if alist[i] > alist[i+gap]:
                    alist[i], alist[i+gap] = alist[i+gap], alist[i]
                i += 1
    return alist
