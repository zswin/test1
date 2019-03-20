#coding=utf-8
__author__ = 'zs'
import random
import time

def dice():
    player = random.randint(1,6)
    print("you rolled:" + str(player))

    print("AI is rolling...")
    ai = random.randint(1,6)
    time.sleep(2)
    print("AI rolled:" + str(ai))

    if ai > player:
        print("you lose")
    elif player > ai:
        print("you win!")
    else:
        print("draw!")

    print("Play again(Y/N)?")
    cont = input()
    print(cont.upper())
    if cont.upper() == 'N':
        exit()
    elif cont.upper() == 'Y':
        pass
    else:
        print("please enter Y or N")

if __name__ == '__main__':
    while True:
        print("please enter to roll")
        roll = input()
        dice()