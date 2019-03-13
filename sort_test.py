#coding=utf-8
__author__ = 'zs'
def bubble_sort(list):
    count = len(list)
    for i in range(0, count):
        for j in range(i+1, count):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
                print(list)
    return list


if __name__ == '__main__':
    lst = [1,200,2,56,12,45,3]
    print(bubble_sort(lst))