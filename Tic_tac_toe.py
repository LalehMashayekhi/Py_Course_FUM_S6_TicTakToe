from pyfiglet import Figlet

f=Figlet(font="slant")
print(f.renderText('text to render'))

def show_game_board():
    for row in game_board:
        for cell in row:
            print(cell,end=" ")
        print()

def check_for_winner(winner):
    for i in range (3):
        if game_board[i][0]==game_board[i][1]==game_board[i][2]=="X":
            winner="X"
            return winner
        elif game_board[i][0]==game_board[i][1]==game_board[i][2]=="O":
            winner="O"
            return winner
        elif game_board[0][i]==game_board[1][i]==game_board[2][i]=="X":
            winner="X"
            return winner
        elif game_board[0][i]==game_board[1][i]==game_board[2][i]=="O":
            winner="O"
            return winner
        elif game_board[0][0]==game_board[1][1]==game_board[2][2]=="X":
            winner="X"
            return winner
        elif game_board[0][0]==game_board[1][1]==game_board[2][2]=="O":
            winner="O"
            return winner
        elif game_board[0][2]==game_board[1][1]==game_board[2][0]=="X":
            winner="X"
            return winner
        elif game_board[0][2]==game_board[1][1]==game_board[2][0]=="O":
            winner="O"
            return winner
    return 1


game_board=[ ["-","-","-"],
                        ["-","-","-"],
                        ["-","-","-"] ]

show_game_board()
while True:
    
    print("Player 1")
    while True:
        row= int(input("Enter row: "))
        col=int(input("Enter colunm:  "))
        if 0<= row <=2 and  0<= col <=2:
            if (game_board[row][col] == "-"):
                game_board[row][col]="X"
                break
            else:
                print("Try Again...") 
        else:
            print("Select in range 0 to 2...")
    show_game_board()
    final_winner=check_for_winner(0)
    if final_winner=="X":
        print("Player 1 wines !!!")
        break

        
    print("player 2")
    while True:
        row= int(input("Enter row: "))
        col=int(input("Enter colunm: "))
        if  0<=row <=2  and 0<=col<=2:
            if (game_board[row][col]=="-"):
                game_board[row][col]="O"
                break
            else:
                print("Try Again...") 
        else:
            print("Select in range 0 to 2...")
    show_game_board()
    final_winner=check_for_winner(0)
    if final_winner=="O":
        print("Player 2 wines !!!")
        break
    
    
