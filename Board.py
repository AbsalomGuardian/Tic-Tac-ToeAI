
class Board:
    ''' Implementation of a tic-tac-toe board class.
        A board is implemented as a dictionary, where keys are cell labels
        and values are cell marks 'X' or 'O' or empty ' '.'''

    def __init__(self):
        '''Sets an empty board.'''
        self.__board = {chr(65 + i) + str(j):' ' for i in range(3) for j in range(1,4)} #[A,C][1,3]
        self.__winner = None


    @property
    def all_moves(self):
        return self.__board.keys()

    @property
    def valid_moves(self):
        '''Returns valid moves on the board that are empty cells.'''
        return [k for k in self.__board.keys() if self.isempty(k)]

    @property
    def winner(self):
        '''Returns the mark of the winner 'X', 'O', or None.'''
        return self.__winner

    def __setitem__(self, cell, mark):
        ''' Marks a cell with 'X' or 'O'.'''
        cell = str(cell).capitalize()
        mark = mark.capitalize()
        self.__board.update({cell : mark})


    def __getitem__(self, cell):
        '''Returns the mark of the cell.'''
        cell = cell.capitalize()
        return self.__board.get(cell)

    def isempty(self, cell):
        ''' Returns True if the cell is empty.'''
        cell = cell.capitalize()
        if self.__board.get(cell) == " ":
            return True
        else:
            return False


    @property
    def isdone(self):
        '''Returns True if one of the game terminating conditions is present. Also sets the winner property.'''
        self.__winner = None
        #check if there are no valid moves remaining
        if len(self.valid_moves) == 0:
            #print("The game is a draw.") #don't need this, the game code does this
            return True
        #check each victory condition. code written by going through the grid starting horizontally and writing every victory
        #condition that includes the cell being considered that hasn't been written already
        elif (self["A1"] == self["B1"]) and  (self["A1"] == self["C1"]) and (self["A1"] != " "):
            #print("Top horizontal victory")
            self.__winner = self["A1"]
            return True
        elif (self["A1"] == self["A2"]) and (self["A1"] == self["A3"]) and (self["A1"] != " "):
            #print("Left vertical victory")
            self.__winner = self["A1"]
            return True
        elif (self["A1"] == self["B2"]) and (self["A1"] == self["C3"]) and (self["A1"] != " "):
            #print("Downward diagonal victory")
            self.__winner = self["A1"]
            return True
        elif (self["B1"] == self["B2"]) and (self["B1"] == self["B3"]) and (self["B1"] != " "):
            #print("Middle vertical victory")
            self.__winner = self["B1"]
            return True
        elif (self["C1"] == self["C2"]) and (self["C1"] == self["C3"]) and (self["C1"] != " "):
            #print("Right vertical victory")
            self.__winner = self["C1"]
            return True
        elif (self["C1"] == self["B2"]) and (self["C1"] == self["A3"]) and (self["C1"] != " "):
            #print("Upward diagnoal victory")
            self.__winner = self["C1"]
            return True
        elif (self["A2"] == self["B2"]) and (self["A2"] == self["C2"]) and (self["A2"] != " "):
            #print("Middle horizontal victory")
            self.__winner = self["A2"]
            return True
        elif (self["A3"] == self["B3"]) and (self["A3"] == self["C3"]) and (self["A3"] != " "):
            #print("Lower horizontal victory")
            self.__winner = self["A3"]
            return True
        else:
            return False

    def __repr__(self):
        '''Returns a string representation of the board.'''
        #had to copy from the test to make sure it passes
        header = '   A   B   C\n'
        row1 = ' +---+---+---+\n1| ' + self["A1"] + ' | '+ self["B1"] +' | '+ self["C1"] + ' |\n'
        row2 = ' +---+---+---+\n2| '+ self["A2"] +' | '+ self["B2"]+' | '+ self["C2"] + ' |\n'
        row3 = ' +---+---+---+\n3| '+ self["A3"]+' | '+self["B3"]+' | '+self["C3"]+' |\n +---+---+---+\n'
        table = header + row1 + row2 + row3
        return table

    def show(self):
        '''Prints the board to the stdout (on the screen).'''
        print(self)

    def __iter__(self):
        '''Returns an iterator of the board.'''
        return iter(self.__board)