#coding=utf-8
def find_prime(n):
    for i in range(2, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print('%d is a prime'%i)

if __name__ == '__main__':
    find_prime(10)