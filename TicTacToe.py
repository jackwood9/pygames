import random
# (0= empty, 1 = x, 2 = o)
global a1, a2, a3, b1, b2, b3, c1, c2, c3, gameisgoing , i3
a1 = 0 
a2 = 0
a3 = 0
b1 = 0
b2 = 0
b3 = 0
c1 = 0
c2 = 0
c3 = 0
gameisgoing = True
i3 = 0
def winstate():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, gameisgoing , i3
    if a1 == 1 and b1 == 1 and c1 == 1:
            print("Player 1 won!")
            gameisgoing = False
    elif a1 == 2 and b1 == 2 and c1 == 2:
            print("Player 2 won!")
            gameisgoing = False
    elif a2 == 1 and b2 == 1 and c2 == 1:
            print("Player 1 won!")
            gameisgoing = False
    elif a2 == 2 and b2 == 2 and c2 == 2:
            print("Player 2 won!")
            gameisgoing = False
    elif a3 == 1 and b3 == 1 and c3 == 1:
            print("Player 1 won!")
            gameisgoing = False
    elif a3 == 2 and b3 == 2 and c3 == 2:
            print("Player 2 won!")
            gameisgoing = False
    elif a1 == 1 and a2 == 1 and a3 == 1:
            print("Player 1 won!")
            gameisgoing = False
    elif a1 == 2 and a2 == 2 and a3 == 2:
            print("Player 2 won!")
            gameisgoing = False
    elif b1 == 1 and b2 == 1 and b3 == 1:
            print("Player 1 won!")
            gameisgoing = False
    elif b1 == 2 and b2 == 2 and b3 == 2:
            print("Player 2 won!")
            gameisgoing = False
    elif c1 == 1 and c2 == 1 and c3 == 1:
            print("Player 1 won!")
            gameisgoing = False
    elif c1 == 2 and c2 == 2 and c3 == 2:
            print("Player 2 won!")
            gameisgoing = False
    elif a1 == 1 and b2 == 1 and c3 == 1:
            print("Player 1 won!")
            gameisgoing = False
    elif a1 == 2 and b2 == 2 and c3 == 2:
            print("Player 2 won!")
            gameisgoing = False
    elif a3 == 1 and b2 == 1 and c1 == 1:
            print("Player 1 won!")
            gameisgoing = False
    elif a3 == 2 and b2 == 2 and c1 == 2:
            print("Player 2 won!")
            gameisgoing = False
    elif a1 != 0 and a2 != 0 and a3 != 0 and b1 != 0 and b2 != 0 and b3 != 0 and c1 != 0 and c2 != 0 and c3 != 0:
            print("Draw!")
            gameisgoing = False
def winstateM():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, gameisgoing , i3
    if a1 == 1 and b1 == 1 and c1 == 1:
            print("Player won!")
            gameisgoing = False
    elif a1 == 2 and b1 == 2 and c1 == 2:
            print("Robot won!")
            gameisgoing = False
    elif a2 == 1 and b2 == 1 and c2 == 1:
            print("Player won!")
            gameisgoing = False
    elif a2 == 2 and b2 == 2 and c2 == 2:
            print("Robot won!")
            gameisgoing = False
    elif a3 == 1 and b3 == 1 and c3 == 1:
            print("Player won!")
            gameisgoing = False
    elif a3 == 2 and b3 == 2 and c3 == 2:
            print("Robot won!")
            gameisgoing = False
    elif a1 == 1 and a2 == 1 and a3 == 1:
            print("Player won!")
            gameisgoing = False
    elif a1 == 2 and a2 == 2 and a3 == 2:
            print("Robot won!")
            gameisgoing = False
    elif b1 == 1 and b2 == 1 and b3 == 1:
            print("Player won!")
            gameisgoing = False
    elif b1 == 2 and b2 == 2 and b3 == 2:
            print("Robot won!")
            gameisgoing = False
    elif c1 == 1 and c2 == 1 and c3 == 1:
            print("Player won!")
            gameisgoing = False
    elif c1 == 2 and c2 == 2 and c3 == 2:
            print("Robot won!")
            gameisgoing = False
    elif a1 == 1 and b2 == 1 and c3 == 1:
            print("Player won!")
            gameisgoing = False
    elif a1 == 2 and b2 == 2 and c3 == 2:
            print("Robot won!")
            gameisgoing = False
    elif a3 == 1 and b2 == 1 and c1 == 1:
            print("Player won!")
            gameisgoing = False
    elif a3 == 2 and b2 == 2 and c1 == 2:
            print("Robot won!")
            gameisgoing = False
    elif a1 != 0 and a2 != 0 and a3 != 0 and b1 != 0 and b2 != 0 and b3 != 0 and c1 != 0 and c2 != 0 and c3 != 0:
            print("Draw!")
            gameisgoing = False
def grid():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, gameisgoing
    print("   1 2 3")
    print("a:", a1, a2, a3)
    print("b:",b1, b2, b3)
    print("c:",c1, c2, c3)
def Easy():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, gameisgoing, i3
    while gameisgoing == True:
        grid()
        e1 = random.randrange(1, 9)
        
        i3 += 1
        i2 = input(f"Move {i3}? ")
        if i2 == "a1":
            a1 = 1
        elif i2 == "a2":
            a2 = 1
        elif i2 == "a3":
            a3 = 1
        elif i2 == "b1":
            b1 = 1
        elif i2 == "b2":
            b2 = 1
        elif i2 == "b3":
            b3 = 1
        elif i2 == "c1":
            c1 = 1
        elif i2 == "c2":
            c2 = 1
        elif i2 == "c3":
            c3 = 1
        elif i2 == "quit" or "Quit":
            gameisgoing = False
        if e1 == 1 and a1 == 0:
            a1 = 2
        elif e1 == 2 and a2 == 0:
            a2 = 2
        elif e1 == 3 and a3 == 0:
            a3 = 2
        elif e1 == 4 and b1 == 0:
            b1 = 2
        elif e1 == 5 and b2 == 0:
            b2 = 2
        elif e1 == 6 and b3 == 0:
            b3 = 2
        elif e1 == 7 and c1 == 0:
            c1 = 2
        elif e1 == 8 and c2 == 0:
            c2 = 2
        elif e1 == 9 and c3 == 0:
            c3 = 2
        else:
            if a1 == 0:
                a1 = 2
            elif a2 == 0:
                a2 = 2
            elif a3 == 0:
                a3 = 2
            elif b1 == 0:
                b1 = 2
            elif b2 == 0:
                b2 = 2
            elif b3 == 0:
                b3 = 2
            elif c1 == 0:
                c1 = 2
            elif c2 == 0:
                c2 = 2
            elif c3 == 0:
                c3 = 2
        winstate()
def Multiplayer():
    global a1, a2, a3, b1, b2, b3, c1, c2, c3, gameisgoing, i3
    while gameisgoing == True:
        grid()
        winstateM()
        #Inputs
        i3 += 1
        i2 = input(f"Player 1 Move {i3}? ")
        if i2 == "a1":
            a1 = 1
        elif i2 == "a2":
            a2 = 1
        elif i2 == "a3":
            a3 = 1
        elif i2 == "b1":
            b1 = 1
        elif i2 == "b2":
            b2 = 1
        elif i2 == "b3":
            b3 = 1
        elif i2 == "c1":
            c1 = 1
        elif i2 == "c2":
            c2 = 1
        elif i2 == "c3":
            c3 = 1
        elif i2 == "quit" or "Quit":
            gameisgoing = False
        grid()
        winstateM()
        i2 = input(f"Player 2 Move {i3}? ")
        if i2 == "a1":
            a1 = 2
        elif i2 == "a2":
            a2 = 2
        elif i2 == "a3":
            a3 = 2
        elif i2 == "b1":
            b1 = 2
        elif i2 == "b2":
            b2 = 2
        elif i2 == "b3":
            b3 = 2
        elif i2 == "c1":
            c1 = 2
        elif i2 == "c2":
            c2 = 2
        elif i2 == "c3":
            c3 = 2
        elif i2 == "quit" or "Quit":
            gameisgoing = False
        
    else:
        gameisgoing =False
difficulty = input("Easy or Multiplayer? ")
if difficulty == "Easy":
    Easy()
elif difficulty == "Multiplayer":
    Multiplayer()
else:
    gameisgoing=False