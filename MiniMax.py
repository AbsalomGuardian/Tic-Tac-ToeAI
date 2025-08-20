from AI import AI

class MiniMax(AI):
    '''Implementation of a tic-tac-toe MiniMax AI class based on a minimax algorithm.'''

    def nextmove(self, board):
        '''Returns the next player's move.'''
        #if board is completely empty, returns the center move instead of using the algorithm
        if len(board.valid_moves) == 9:
            return "B2"
        return self.minimax(board, True, True)

    def minimax(self, board, isplayer, start):
        '''Returns a valid player's move.'''
        #base condition, the game is done
        if board.isdone:                  # check the base condition
            if board.winner == self.mark: # the player won the game
                return 1
            elif board.winner == None:    # the game is a tie
                return 0
            else:
                return -1                 # the player lost the game

        #"Set the min score to infinity (or a number greater than 1) and max score to -infinity(or a number less than -1)."
        maxScore, minScore = -10, 10
        bestMove = None

        #"Iterate through all valid moves:"
        for i in board.valid_moves:
            #"If it is the player's turn:"
            if isplayer:
                #"Mark the cell with the player's mark."
                board[i] = self.mark
                #"Get the score by calling minimax recursively (the opponent must take the next turn)."
                newScore = self.minimax(board, False, False)
                #"Update the max score if the new scoreis greater."
                if newScore >= maxScore:
                    maxScore = newScore
                    #"Update the best move"
                    bestMove = i

             #"If it is the opponent's turn:"
            else:
                #"Mark the cell with the opponent's mark."
                board[i] = self.antimark
                #"Get the score by calling minimax recursively (the player must take the next turn)."
                newScore = self.minimax(board, True, False)
                #"Update the min score if the new score is lesser."
                if newScore <= minScore:
                    minScore = newScore
                    #"Update the best move."
                    bestMove = i
            #Unmark the cell (make it an empty cell) and reset all other variables that were affected by the previous game play.
            board[i] = " "




        if start:
            return bestMove
        elif isplayer:
            return maxScore
        else:
            return minScore