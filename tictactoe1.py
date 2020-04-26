#I worked on this with my Dad 
theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }

board_keys = []

for key in theBoard:
    board_keys.append(key)
#Creating the board (after I had to draw it out on paper to visualize it) 
def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])


def game():

    turn = 'X'
    count = 0

#Naming the box locations by their spot 
    for i in range(10):
        printBoard(theBoard)
        print("Your turn, " + turn + ".Pick a spot 1-9")

        move = input()        

        if theBoard[move] == ' ':
            theBoard[move] = turn
            count += 1
        else:
            print("That spot has been taken.\nSelect another spot.")
            continue

 #These are the ways to win the game with the boxes they represent       
        if count >= 5:
            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': 
                printBoard(theBoard)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 


        if count == 9:
            print("Game Over.")                
            print("You tied!")


        if turn =='X':
            turn = 'O'
        else:
            turn = 'X'        
    
    restart = input("Do want to play Again?(yes/no)")
    if restart == "yes" or restart == "Yes":  
        for key in board_keys:
            theBoard[key] = " "


        game()

if __name__ == "__main__":
    game()
