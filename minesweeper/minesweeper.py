import random
from menu import *


SIZE_BATTLE_FIELD = LVL
LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I','J','K','L','M','N','O']
L = '   A   B   C   D   E   F   G   H   I   J   K   L   M   N   O'
NUMS = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
EMPTY = ' '
SQUARE = '■'
BOMB = '*'
BATTLE_FIELD_USER = []
BATTLE_FIELD_REAL = []

def createBattleField_U():
    for row in range(SIZE_BATTLE_FIELD):
        tmp = []
        for col in range(SIZE_BATTLE_FIELD):
            tmp.append(EMPTY)
        BATTLE_FIELD_USER.append(tmp)

def createBattleField_R():
    for row in range(SIZE_BATTLE_FIELD):
        tmp = []
        for col in range(SIZE_BATTLE_FIELD):
            tmp.append(EMPTY)
        BATTLE_FIELD_REAL.append(tmp)

def printBattleFieldU(level):

    for j in range(level):
        if j != level - 1:
            print(" ",LETTERS[j], end= " ")
        else:
            print("  ", LETTERS[j])

    for i, row in enumerate(BATTLE_FIELD_USER):
        print(NUMS[i], end=' ')
        for j in row:
            if j == SQUARE:
                print(f'\x1b[32m {j} \033[0m', end=' ')
            elif j == BOMB:
                print(f'\x1b[31m {j} \033[0m', end=' ')
            else:
                print(f'\x1b[33m '" "' \033[0m', end=' ')
        print(NUMS[i])
    for k in range(level):
        if k != level - 1:
            print(" ", LETTERS[k], end=" ")
        else:
            print("  ", LETTERS[k])


def printBattleFieldR():
    with open('small_hint.txt', 'w') as file:
        file.write(L+'\n')
        for i, row in enumerate(BATTLE_FIELD_REAL):
            line = ' '.join(f' {j} ' for j in row)
            file.write(f'{NUMS[i]} {line} {NUMS[i]}\n')
        file.write(L)

def bombsSet(AMOUNT):
    for i in range(AMOUNT):
        while True:
            pos_h = random.randint(1, SIZE_BATTLE_FIELD-1)
            pos_v = random.randint(1, SIZE_BATTLE_FIELD-1)
            if BATTLE_FIELD_REAL[pos_h][pos_v] == EMPTY:
                BATTLE_FIELD_REAL[pos_h][pos_v] = BOMB
                break

def goTo(level):
    while True:
        your_pos_h = input(f"Enter horizontal position (from {LETTERS[0]} to {LETTERS[level-1]}) \n-> ")
        your_pos_v = input(f"Enter vertical position (from {NUMS[0]} to {NUMS[level-1]}) \n-> ")

        if your_pos_h not in LETTERS or your_pos_v not in NUMS:
            print("Invalid inputs! Try again!")
            continue

        pos_h = LETTERS.index(your_pos_h)
        pos_v = int(your_pos_v) - 1

        if BATTLE_FIELD_USER[pos_v][pos_h] == SQUARE:
            print("Position already selected. Please try again.")
            continue

        if BATTLE_FIELD_REAL[pos_v][pos_h] == BOMB :
            BATTLE_FIELD_USER[pos_v][pos_h] = BOMB
            print("Game Over! You hit a bomb.")

            printBattleFieldU(level)

            return

        if BATTLE_FIELD_USER[pos_v][pos_h] == EMPTY and BATTLE_FIELD_REAL[pos_v][pos_h] == EMPTY:
            BATTLE_FIELD_USER[pos_v][pos_h] = SQUARE
            BATTLE_FIELD_REAL[pos_v][pos_h] = SQUARE
            printBattleFieldU(level)

def startGame(level):
    global SIZE_BATTLE_FIELD

    SIZE_BATTLE_FIELD = level
    createBattleField_U()
    createBattleField_R()
    printBattleFieldU(level)
    bombsSet(level)
    printBattleFieldR()
    goTo(level)
