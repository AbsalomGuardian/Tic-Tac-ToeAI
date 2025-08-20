from Board import Board
from Player import Player
from AI import AI
from SmartAI import SmartAI
from MiniMax import MiniMax

#This is the file to run
# It will capitalize inputs for mark tho.

def oppositeMark(mark): #returns the opposite mark of the passed mark. used in automatically setting the mark of the second player
    if mark == "O":
        return "X"
    elif mark == "X":
        return "O"
    else:
        print("That wasn't a valid mark. Returning None")
        return None

def isValidMark(mark): #returns true/false if passed mark is valid (X/O)
    if mark == "X" or "O":
        return True
    else:
        return False

print("Welcome to the TIC-TAC-TOE Game!")
needSettings = True #so the program knows this is the first time it has been launched or the player has requested to change the settings instead of just a new game
while True: #loop of the entire program
    board = Board() #reset the board
    #establishing settings of the 
    if needSettings:
        print("Please enter the number of the option you would like:")
        print("1. Player vs Player")
        print("2. Player vs AI")
        print("3. AI vs AI")

        while True: #keep asking for gamemode until input is valid
            try:
                gamemode = int(input())
                if gamemode > 3 or gamemode < 1:
                    print("Please input 1, 2, or 3.")
                else: 
                    break
            except ValueError:
                print("Please input an integer 1, 2, or 3.")
        #print("gamemode is " + str(gamemode))

        if gamemode == 1:
            #print("settings for 1")
            name1 = input("Enter the name of the first player: ")

            while True: #keep asking for mark until recieves valid mark
                try:
                    mark1 = input("Enter the mark of the first player [X/O]: ").upper()
                    if not isValidMark(mark1):
                        print("That isn't a valid mark. Try again.")
                    else: 
                        break
                except ValueError:
                    print("Please input X or O.")

            name2 = input("Enter the name of the second player: ")
            mark2 = oppositeMark(mark1)
            global player1
            player1 = Player(name1, mark1)
            global player2
            player2 = Player(name2, mark2)

        elif gamemode == 2:
            name1 = input("Enter the name of the player (first player): ")

            while True: #keep asking for mark until recieves valid mark
                mark1 = input("Enter the mark of the first player [X/O]: ").upper()
                if isValidMark(mark1):
                    break
                else: print("That isn't a valid mark. Try again.")

            player1 = Player(name1, mark1)
            print("Enter the number of the AI program the opponent should use:")
            print("1. Random AI")
            print("2. MinMax Algorithm")
            print("3. Solved Algorithm")

            while True: #keep asking for input until it is valid
                ai = input()
                if ai == "1" or "2" or "3":
                    break
                else:
                    print("That isn't a valid input. Please enter either 1, 2, or 3")

            mark2 = oppositeMark(mark1)
            if ai == "1":
                player2 = AI("Random", mark2)
            elif ai == "2":
                player2 = MiniMax("MinMax", mark2)
            elif ai == "3":
                player2 = SmartAI("SmartAI", mark2)

        elif gamemode == 3:
            while True: #keep asking for mark until recieves valid mark
                mark1 = input("Enter the mark the player1 AI should use[X/O]: ").upper()
                if isValidMark(mark1):
                    break
                else: print("That isn't a valid mark. Try again.")
            mark2 = oppositeMark(mark1)
            print("Enter the number of the AI program player1 should use:")
            print("1. Random AI")
            print("2. MinMax Algorithm")
            print("3. Solved Algorithm")

            while True: #keep asking for input until it is valid
                ai1 = input()
                if ai1 == "1" or "2" or "3":
                    break
                else:
                    print("That isn't a valid input. Please enter either 1, 2, or 3")

            if ai1 == "1":
                player1 = AI("Random(1)", mark1)
            elif ai1 == "2":
                player1 = MiniMax("MinMax(1)", mark1)
            elif ai1 == "3":
                player1 = SmartAI("SmartAI(1)", mark1)
            
            print("Enter the number of the AI program player2 should use:")
            print("1. Random AI")
            print("2. MinMax Algorithm")
            print("3. Solved Algorithm")

            while True: #keep asking for input until it is valid
                ai2 = input()
                if ai2 == "1" or "2" or "3":
                    break
                else:
                    print("That isn't a valid input. Please enter either 1, 2, or 3")
            
            if ai2 == "1":
                player2 = AI("Random(2)", mark2)
            elif ai2 == "2":
                player2 = MiniMax("MinMax(2)", mark2)
            elif ai2 == "3":
                player2 = SmartAI("SmartAI(2)", mark2)


    turn = True #loop of the game
    while True:
        board.show()
        if turn:
            player1.choose(board)
            turn = False
        else:
            player2.choose(board)
            turn = True
        if board.isdone:
            break
    board.show()
    if board.winner == player1.mark:
        print(f"{player1.name} is the winner!")
    elif board.winner == player2.mark:
        print(f"{player2.name} is the winner!")
    else:
        print("It is a tie!")
    ans = input("Would you like to play again[Y/N]? ").upper() #if not Y, the program ends
    if (ans == "Y"):
        setting = input("Would you like to use the same settings for the next game[Y/N]? ").upper()  #establishes if the uppercoming loop will ask for settings
        if setting == "Y":
            needSettings = True
        else:
            needSettings = False
    if (ans != "Y"):
        break
print("Goodbye!")