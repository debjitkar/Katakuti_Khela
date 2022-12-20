# for displaying the tic tac toe board
def board(a):
    print("",a[1]," │",a[2]," │ ",a[3]," ")
    print("────┼────┼────")
    print("",a[4]," │",a[5]," │ ",a[6]," ")
    print("────┼────┼────")
    print("",a[7]," │",a[8]," │ ",a[9]," ")
    
# for displaying the instruction of game
def instructions():
    print("\n----------- WELCOME TO TIC TAC TOE ------------\n\n")
    board(pos)
    print()
    
    players[0] = input("Enter the name of the Player 1 : ")
    players[1] = input("Enter the name of the Player 2 : ")
    
    print("\n-------- Instructions ---------")
    print("=>>",players[0],"you will be using X")
    print("=>>",players[1],"you will be using O")
    print("=>> Turn starts from",players[0])
    print("=>> Potisions are :-")
    print("  1 │  2 │ 3  ")
    print("────┼────┼────")
    print("  4 │ 5  │ 6  ")
    print("────┼────┼────")
    print("  7 │ 8  │ 9  ")
    print("=>> press S to start the game")
    flag = input()    
    return flag

# for starting the game
def startgame():
    turn = 0
    for i in range(9):
        if turn % 2 == 0:
            print("\nThis is ",players[0],"\'s  turn")
            p = int(input("Please enter the postion : "))
            v = 'X'
            pos[p] = v
            board(pos)
            winner = checkwin(v)
            if winner == "nobody":
                turn = 1
                continue
            else:
                print("\n\n",players[0],"won the game!")
                break
        else:
            print("\nThis is ",players[1],"\'s  turn")
            p = int(input("Please enter the postion : "))
            v = 'O'
            pos[p] = v
            board(pos)
            winner = checkwin(v)
            if winner == "nobody":
                turn = 0
                continue
            else:
                print("\n\n",players[1],"won the game!")    
                break
    else:
        print("\n\nGame Tied!")
        
# checking the winner 
def checkwin(v):
    for i in winning_conditions:
        if (pos[i[0]], pos[i[1]], pos[i[2]]) == (v,v,v):
            winner = players[0]
            break
        elif (pos[i[0]], pos[i[1]], pos[i[2]]) == (v,v,v):
            winner = players[1]
            break
    else:
        winner = "nobody"
    return winner

 
pos = ['',' ',' ',' ',' ',' ',' ',' ',' ',' ']
players = ['','']
winning_conditions = [(1,2,3),(4,5,6),(7,8,9),(1,4,7),(2,5,8),(3,6,9),(1,5,9),(3,5,7)]
flag = instructions()
if flag.lower() == 's':
    startgame()
else:
    print("Invalid Entry")
