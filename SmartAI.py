from AI import AI

class SmartAI(AI):
    '''Implementation of a SmartAI class.
    Overrides nexmove and uses the solved alogirthm for tic-tac-toe. Should always win or at least tie.'''


    def nextmove(self, board):
        '''Returns the next player's move.'''
        #Alogirthm taken from wikipedia:
        #1. Win: If the player has two in a row, they can place a third to get three in a row.
        winMove = self.findAlmost("player", board)
        if(winMove != None):
            return winMove
        #2. Block: If the opponent has two in a row, the player must play the third themselves to block the opponent.
        elif self.findAlmost("opponent", board) != None: #have to run findAlmost twice to be able to use elif
            return self.findAlmost("opponent",board)
        #3. Fork: Cause a scenario where the player has two ways to win (two non-blocked lines of 2).
        elif len(self.findForks("player", board)) != 0:
            return self.findForks("player", board)[0]
        #4a. Blocking an opponent's fork: If there is only one possible fork for the opponent, the player should block it.
        elif len(self.findForks("opponent", board)) > 0 :
            forks = self.findForks("opponent", board)
            if len(forks) == 1:
                return forks[0]
            #4b. Otherwise, the player should block all forks in any way that simultaneously allows them to make two in a row.
            elif self.blockAll(board) != None:
                return self.blockAll(board)
            #4c. Otherwise, the player should make a two in a row to force the opponent into defending, as long as it does not result in
                #them producing a fork.
                #For example, if "X" has two opposite corners and "O" has the center,
                #"O" must not play a corner move to win. (Playing a corner move in this scenario produces a fork for "X" to win.)
                # X _ !
                # _ O _
                #  _ X
            elif self.complicated(board) != None:
                return self.complicated(board)
                
        #5. Center: A player marks the center.
        if("B2" in board.valid_moves):
            return "B2"
        #6. Opposite corner: If the opponent is in the corner, the player plays the opposite corner.
        elif(self.findCorner("opponent", board) != None):
            return self.findCorner("opponent", board)
            #7. Empty corner: The player plays in a corner square.
        else:
            for i in self.corners:
                if i in board.valid_moves:
                    return i
            #8. Empty side: The player plays in a middle square on any of the four sides.
            middles = ["B1", "A2", "B3", "C2"]
            for i in middles:
                if i in board.valid_moves:
                    return i


    #these find places where there are two of the same mark in a row. return where to put a mark to complete/defeat the set.
    #otherwise return None. Target is either "player" or "opponent".
    def findAlmost(self, target, board):
        mark = self.getMark(target)
        #use w or self.places[i] for keys and board[w]/board[self.places[i]] for value
       # print("checking mark: " + mark)
        for i, w in enumerate(self.places):
           # print("checking:" + str(i) + w)
            if board[w] == mark:
                #checking if there's an adjacent (or one over in a row) matching mark, and if so returning the one that completes the set
                    #checking by columns #string slicing isn't working here
                    if w[:1] == "A": #if w is in the leftmost position
                        if (board[self.places[i + 1]] == mark) and (self.places[i + 2] in board.valid_moves) : #check to its right
                            return self.places[i + 2] #return rightmost if empety
                        if (board[self.places[i + 2]] == mark) and (self.places[i + 1] in board.valid_moves) : #check to its right
                            return self.places[i + 1] #return middle if empety

                    elif w[:1] == "B": #if w is in middle position
                        if (board[self.places[i + 1]] == mark) and (self.places[i - 1] in board.valid_moves) : #check to its right
                            return self.places[i - 1] #return leftmost if empty
                        elif (board[self.places[i - 1]] == mark) and (self.places[i + 1] in board.valid_moves): #check to its left
                            return self.places[i + 1] #return rightmost if empty

                    elif w[:1] == "C": #if w is in the rightmost position
                        if (board[self.places[i - 1]] == mark) and (self.places[i - 2] in board.valid_moves): #check middle
                            return self.places[i - 2] #if empty return leftmost positon
                        elif (board[self.places[i - 2]] == mark) and (self.places[i - 1] in board.valid_moves): #check leftmost
                            return self.places[i - 1] #if empty return middle

                    #checking by row
                    if w[1:] == "1": #check top row
                        try: #kept getting out of index errors, but it shouldn't be happening. this fixes that
                                n = board[self.places[i + 6]]
                                n = self.places[i + 3]
                                if (board[self.places[i + 3]] == mark) and (self.places[i + 6] in board.valid_moves): #check one down
                                    return self.places[i + 6] #return bottom if empty
                                elif (board[self.places[i + 6]] == mark) and (self.places[i + 3] in board.valid_moves): #check bottom
                                    return self.places[i + 3] #return middle if empty
                        except:
                            pass

                    elif w[1:] == "2": #check middle row
                        if (board[self.places[i + 3]] == mark) and (self.places[i - 3] in board.valid_moves): #check one down
                            return self.places[i - 3] #return top if empty
                        elif (board[self.places[i - 3]] == mark) and (self.places[i + 3] in board.valid_moves): #check top
                            return self.places[i + 3] #return bottom if empty

                    elif w[1:] == "3": #check bottom row
                        if (board[self.places[i - 3]] == mark) and (self.places[i - 6] in board.valid_moves): #check one above
                            return self.places[i + 6] #return top if empty
                        elif (board[self.places[i - 6]] == mark) and (self.places[i - 3] in board.valid_moves): #check top
                            return self.places[i - 3] #return middle if empty

                    #check corners
                    if w in self.corners:
                        #middle either has to have mark or be empty
                        if "B2" in board.valid_moves: #if middle is free, check that there are matching marks in opposite corners
                            for j, x in enumerate(self.corners):
                                if j == 0 or 2: #is x's pair to its right
                                    if (x == w) and (board[self.corners[j + 1]] == mark):
                                        return "B2"
                                else: #if x's pair is to its left
                                    if (x == w) and (board[self.corners[j - 1]] == mark):
                                        return "B2"
                        elif board["B2"] == mark: #if middle is taken, check opposite corner is free and if so, return opposite corner
                            for j, x in enumerate(self.corners):
                                if j == 0 or 2: #is x's pair to its right
                                    try:
                                        if (x == w) and (self.corners[j + 1] in board.valid_moves):
                                            return self.corners[j + 1]
                                    except: pass
                                else: #if x's pair is to its left
                                    if (x == w) and (self.corners[j - 1] in board.valid_moves):
                                        return self.corners[j - 1]


    #returns a list of all the moves the player or the opponent has made. Target is either "player" or "opponent".
    #might not actually need this
    def playedMoves(self, target, board): #append all the places with the mark of the target
        mark = self.getMark(target)
        moves = []
        for w in self.places:
            if board[w] == self.mark:
                moves.append(w)
        return moves

    #returns all points someone could put a mark to create a fork
    def findForks(self, target, board):
        doubles = self.findDoubles(target, board)
        forks = set() #forks is a set so that duplicates are automatically removed
        #a potentional fork is where the second place appears twice
        p1, p2 = map(list, zip(*doubles)) #unpack doubles
        #print(p2)
        #append all second points that appear more than once to forks
        for w in p2:
            #print("checking: " + w)
            if  p2.count(w) > 1:
                forks.add(w)

        forks = list(forks) #convert to a list, what I'm used to working in for this entire program
        return forks

    #returns as a list of 2-tuples, all possible two in a row that can be created, last one is potentional
    #this includes with spaces, so an X in A1 in an otherwise empty top row will return (A1, B1) and (A1, C1).
    #since you're never going to call this function when findAlmost returns anything, it will not be checking to see if the proper mark is
    #already placed anywhere
    def findDoubles(self, target, board):
        doubles = []
        mark = self.getMark(target)
        for i, w in enumerate(self.places): #need to use all places as list here
            if board[w] == mark: #copied from findAlmost's code and modified
                    #checking by columns
                    if w[:1] == "A": #if w is in the leftmost position
                        if self.places[i + 2] in board.valid_moves and self.places[i + 1] in board.valid_moves: #if that horizontal row is still valid victory
                            doubles.append((w, self.places[i + 2]))
                            doubles.append((w, self.places[i + 1]))

                    elif w[:1] == "B": #if w is in middle position
                        if self.places[i - 1] in board.valid_moves and self.places[i + 1] in board.valid_moves:
                            doubles.append((w, self.places[i - 1]))
                            doubles.append((w, self.places[i + 1]))

                    elif w[:1] == "C": #if w is in the rightmost position
                        if self.places[i - 2] in board.valid_moves and self.places[i - 1] in board.valid_moves:
                            doubles.append((w, self.places[i - 2]))
                            doubles.append((w, self.places[i - 1]))

                    #checking by row
                    if w[1:] == "1": #check top row
                        try: #kept getting out of index errors, but it shouldn't be happening. this fixes that
                                n = board[self.places[i + 6]]
                                n = self.places[i + 3]
                                if self.places[i + 6] in board.valid_moves and self.places[i + 3] in board.valid_moves: #check bottom
                                    doubles.append((w, self.places[i + 6])) #return bottom if empty
                                    doubles.append((w, self.places[i + 3])) #return middle if empty
                        except:
                            pass

                    elif w[1:] == "2": #check middle row
                        if self.places[i - 3] in board.valid_moves and self.places[i + 3] in board.valid_moves: #check top
                            doubles.append((w, self.places[i - 3])) #return top if empty
                            doubles.append((w, self.places[i + 3])) #return bottom if empty

                    elif w[1:] == "3": #check bottom row
                        if self.places[i - 6] in board.valid_moves and self.places[i - 3] in board.valid_moves: #check top
                            doubles.append((w, self.places[i - 6]))
                            doubles.append((w, self.places[i - 3]))

                    #check corners
                    if w in self.corners:
                        #both middle and opposite corner needs to be empty
                        if "B2" in board.valid_moves:
                            #can't make this work algorthimatically, so have it hardcoded
                            if (w == "A1") and ("C3" in board.valid_moves):
                                doubles.append((w, "B2"))
                                doubles.append((w, "C3"))
                            elif (w == "C3") and ("A1" in board.valid_moves):
                                doubles.append((w, "B2"))
                                doubles.append((w, "A1"))
                            elif (w == "C1") and ("A3" in board.valid_moves):
                                doubles.append((w, "A3"))
                                doubles.append((w, "B2"))
                            elif (w == "A3") and ("C1" in board.valid_moves):
                                doubles.append((w, "A3"))
                                doubles.append((w, "B2"))

                    #check middle
                    if w == "B2":
                        for i in self.corners:
                            if "A1" in board.valid_moves and "C3" in board.valid_moves:
                                doubles.append((w, "A1"))
                                doubles.append((w, "C3"))
                            if "C1" in board.valid_moves and "A3" in board.valid_moves:
                                doubles.append((w, "A3"))
                                doubles.append((w, "C1"))

        if len(doubles) == 0: #to prevent errors before each person has gone once
            doubles.append((None, None))
        return doubles





    #returns the opposite corner of a corner that has specified mark
    def findCorner(self, target, board):
        mark = self.getMark(target)
        for j, x in enumerate(self.corners):
            if board[x] == mark:
                if j == 0 or 2:
                    return self.corners[j + 1]
                else:
                    return self.corners[j - 1]

    def getMark(self, target):
        #returns what mark the function should be considering
        if target == "player":
            mark = self.mark
        else:
            mark = self.opponent_mark
        return mark

    #directly impliments part of the alogirthm and returns a move:  #Otherwise, the player should
        #block all forks in any way that simultaneously allows them to make two in a row.
    def blockAll(self, board):
        d1, d2 = map(list, zip(*self.findDoubles("player", board))) #move needs to be in d2
        forks = self.findForks("opponent", board) #for blockAll to be called there needs to be more than one fork
        if forks[0] == None and d2[0] == None: #if none of this has happened, end this method
            return None
        blockables = forks #all spaces you could put a mark to block a fork. includes the fork locations as well as any directly adjacent to it
        for w in forks:
          blockables = blockables + self.findAdjacent(w, board) #cocatonate
        #actually test each of the proposed blockables
        for j in blockables:
           # print("test place (blockall): " + j)
            board[j] = self.mark
            if len(self.findForks("opponent", board)) == 0 and j in d2: #check if it defeats all of the forks and creates 2 in a row
                board[j] = " " #still need to remove change
                return j
            board[j] = " " #still need to remove change
        else: #if condition is never fufilled, return None
            return None

    #return list of all places directly adjacent to the passed place, which are also empty
    def findAdjacent(self, p, board):
        #based on findAlmost
        adjacents = []
        i = self.places.index(p) #find the index of p within places
        #checking by columns
        if p[:1] == "A": #if p is in the leftmost position
                if self.places[i + 1] in board.valid_moves: #record middle
                    adjacents.append(self.places[i + 1])

        elif p[:1] == "B": #if p is in the middle position
                if self.places[i - 1] in board.valid_moves: #record left
                    adjacents.append(self.places[i - 1])
                if self.places[i + 1] in board.valid_moves: #record right
                    adjacents.append(self.places[i + 1])

        elif p[:1] == "C": #if p is in the rightmost position
                if self.places[i - 1] in board.valid_moves: #record middle
                    adjacents.append(self.places[i - 1])

        #checking by row
        if p[1:] == "1": #check top row
            try: #kept getting out of index errors, but it shouldn't be happening. this fixes that
                n = self.places[i + 3]
                if self.places[i + 3] in board.valid_moves: #check middle    
                    adjacents.append(self.places[i + 3]) 
            except:
                pass

        elif p[1:] == "2": #check middle row
            if self.places[i - 3] in board.valid_moves: #top
                adjacents.append(self.places[i - 3])
            if self.places[i + 3] in board.valid_moves: #bottom
                adjacents.append(self.places[i + 3]) 

        elif p[1:] == "3": #check bottom row
            if self.places[i - 3] in board.valid_moves: #check middle
                adjacents.append(self.places[i - 3])

        #check corners
        if p in self.corners:
            if "B2" in board.valid_moves: #check middle
                adjacents.append("B2")
        #check middle
        if p == "B2":
            for i in self.corners:
                if i in board.valid_moves:
                    adjacents.append(i)

        return adjacents

    def complicated(self, board):
        #does 4c. In short, create 2 in a row, as long as the third one isn't a fork location for the opponent
        #returns the move, only works for player
        d1, d2 = map(list, zip(*self.findDoubles("player", board)))
        forks = self.findForks("opponent", board)
        
        if d2[0] == None: #end all this if there were no doubles
            return None
        #what to do, test place each of d2, then find almost with that board as see if what almost returns is in forks
        for i in d2:
            #print("test place (complicated): " + i)
            board[i] = self.mark
            nextMove = self.findAlmost("player", board)
            if nextMove != None and nextMove not in forks:
                board[i] = " "
                return i
            board[i] = " "
        return None