# coding=utf-8
__author__ = 'zs'

def select_sort(lst):
    count = len(lst)
    for i in range(0, count):
        min_idx = i
        for j in range(i+1, count):
            if lst[j] < lst[min_idx]:
                min_idx = j
        if i != min_idx:
            lst[i], lst[min_idx] = lst[min_idx], lst[i]
            print(lst)

    return lst


if __name__ == '__main__':
    print(select_sort([9,1,5,8,3,7,4,6,2]))
