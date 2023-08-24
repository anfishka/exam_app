directions = ['w','s']
range_lvl = [['light', 5],['medium', 10], ['hard', 15]]
current_pos = 0
min_pos = 0
max_pos = len(range_lvl)
LVL = range_lvl[0][1]

def printMenu():
    global current_pos
    for k in range(1):
        print("*" * 50)
        for i in range(len(range_lvl)):
            if i == current_pos:
                print("\t" * 5  + f"\033[93m-> {range_lvl[i][0]}\033[00m", )
            else:
                print("\t" * 5 , range_lvl[i][0])
        print("*" * 50)
def menuChoose():
    global current_pos, range_lvl, LVL
    print(f"Choose an option from menu, using {directions[0]} to go up, and {directions[1]} to go down, press ENTER btn to start game, if you made a choice ")
    print("Menu ->")
    printMenu()

    min_pos = 0
    max_pos = len(range_lvl) - 1

    while True:
        option = input("Choose -> ")
        if option.lower() == directions[0] and current_pos <= max_pos and current_pos >= min_pos:
            current_pos = current_pos - 1
            printMenu()

        if option.lower() == directions[1] and current_pos <= max_pos and current_pos >= min_pos:
            current_pos = current_pos + 1
            printMenu()
        if option == '':
            LVL = range_lvl[current_pos][1]
            return LVL

        if current_pos > max_pos:
            current_pos = max_pos
            printMenu()
        elif current_pos < min_pos:
            current_pos = min_pos
            printMenu()