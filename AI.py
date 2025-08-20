from Player import Player
from random import choice

class AI(Player):
    '''Implementation of a tic-tac-toe AI player class.
    Default method of choosing a new move is random. Child classes will have better algorithms.'''

    @property
    def opponent_mark(self): #should be using this instead of antimark but whatever
        '''Returns the opponent's mark.'''
        if self.mark == "X":
            return "O"
        else:
            return "X"
        ## YOUR CODE ##

    def nextmove(self, board): #commenting this out breaks the simple AI, but will fix inheritance if that's the problem
        '''Returns the next player's move. Which is randomly selected from all valid moves'''
        validMoves = board.valid_moves
        return choice(validMoves)
        ## YOUR CODE ##

    def choose(self, board):
        '''Prints the prompt and the player's move and marks the cell on the board.'''
        cell = self.nextmove(board)
        #print("marking" + cell)
        board[cell] = self.mark
        print(f'{self.name}, {self.mark}: Enter a cell [A-C][1-3]: {cell}')


