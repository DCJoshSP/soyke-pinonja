from random import randint
import os
import time
credit = float(1)
symbol = []
skull = 0
bell = 0
quit = False
symbols = ["Cherry", "Bell", "Lemon", "Orange", "Star", "Skull"]
print("You have:", credit)
x = input("Press ENTER to continue")
while quit == False:
    credit = credit - 0.2
    for count in range(0,2):
        print("/ / /")
        time.sleep(0.25)
        os.system("cls")
        print("| | |")
        time.sleep(0.25)
        os.system("cls")
        print("\ \ \\")
        time.sleep(0.25)
        os.system("cls")
    for i in range(0, 3):
        random = randint(0, 5)
        symbol.append(symbols[random])
        print(symbol[i])
    #next
    for s in symbol:
        if s == "Bell":
            bell = bell + 1
        elif s == "Skull":
            skull = skull + 1
        #end if
    #next
    if skull == 3:
        print("You loose!")
        credit = 0
    elif skull == 2:
        print("You loose £1!")
        credit = credit - 1
    elif bell == 3:
        print("You win £5")
        credit = credit + 5
    elif symbol [0] == symbol[1] and symbol[1] == symbol[2]:
        print("You win £1!")
        credit = credit + 1
    elif symbol[0] == symbol[1] or symbol[0] == symbol[2] or symbol[1] == symbol[2]:
        print("You win 50p!")
        credit = credit + 0.5
    #end if
    symbol = []
    bell = 0
    skull = 0
    print("You have:", round(credit, 2), "left")
    if credit < 0:
        quit = True
    #end if
    ans = input("Do you want to play again? Y/N ")
    os.system("cls")
    if ans == "N":
        quit = True
    #end if
#end while






