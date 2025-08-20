class Player:
    '''Implementation of a tic-tac-toe Player class.'''
    def __init__(self, name, mark, board=None): 
        '''Player's name and mark are required arguments. A board is optional.'''
        self.__name = name  # player's name
        mark.upper()
        self.__mark = mark  # player's mark is 'O' or 'X'
        self.__board = board
    

        #variables for the smartAI class, that have to be here so inheritance works correctly
        self.places = ["A1", "B1", "C1", "A2", "B2", "C2", "A3", "B3", "C3"] #simple list of all the cordinate pairs, to allow stuff like board[self.places[i + 1]]
        self.corners = ["A1", "C3", "A1", "C3"] #corner pairs right next to eachother


    @property
    def name(self):
        '''Returns the player's name.'''
        return self.__name

    @property
    def mark(self):
        '''Returns the player's mark.'''
        return self.__mark

    def choose(self, board):
        ''' Prompts the user to choose a cell.
        If the user enters a valid string and the cell on the board is empty, updates the board.
        Otherwise, prints a message that the input is wrong and reprints the prompt.'''

        while True:
            cell = input(f'{self.__name}, {self.__mark}: Enter a cell [A-C][1-3]:').upper()
            if cell in board.valid_moves:
                    board[cell] = self.mark
                    break
            else:
                    print('You did not choose correctly.')