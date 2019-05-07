#coding=utf-8
__author__ = 'zs'
def bubble_sort(list):
    count = len(list)
    for i in range(0, count):
        for j in range(i+1, count):
            print("(" + str(i) + ")" + str(list[i]), "(" + str(j) + ")" + str(list[j]))
            if list[i] > list[j]:

                a = str(list[i]) + '<->' + str(list[j])
                list[i], list[j] = list[j], list[i]
                print(a, list)
            else:
                print(str(list[i]) + "<="+ str(list[j]))
    return list


def bubble_sort2(lst):
    count = len(lst)
    for i in range(0, count):
        for j in range(count-2, i-1, -1):
            print("(" + str(j) + ")" + str(lst[j]), "(" + str(j+1) +")" + str(lst[j+1]))
            if lst[j] > lst[j+1]:
                print(str(lst[j]) + "<->" + str(lst[j+1]))
                lst[j], lst[j+1] = lst[j+1], lst[j]
                print(lst)

    return lst


def bubble_sort3(lst):
    count = len(lst)
    flag = True
    for i in range(0, count):
        if not flag:
            continue
        else:
            flag = False
        for j in range(count-2, i-1, -1):
            print("(" + str(j) + ")" + str(lst[j]), "(" + str(j+1) +")" + str(lst[j+1]))
            if lst[j] > lst[j+1]:
                flag = True
                print(str(lst[j]) + "<->" + str(lst[j+1]))
                lst[j], lst[j+1] = lst[j+1], lst[j]
                print(lst)

    return lst


if __name__ == '__main__':
    lst = [9,1,5,8,3,7,6,2]
    print("final result:", bubble_sort2(lst))