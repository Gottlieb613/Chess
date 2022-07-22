import numpy as np
from Piece import *
# I was thinking we would have an object for the board itself
# and maybe some for pieces and the gameplay and then the GUI. idk we'll figure it out

class Board:
    state = None 
    
    def __init__(self):
        self.setup_board()
        pass

    def print_board(self):
        b = self.state
        # {
        #         1: ['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R'],
        #         2: ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        #         3: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        #         4: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        #         5: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        #         6: [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        #         7: ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
        #         8: ['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R'],
        # }
        outline = '+---+---+---+---+---+---+---+---+'
        for i in range(8):
            print(outline)
            print(f"| {b[i][0]} | {b[i][1]} | {b[i][2]} | {b[i][3]} | {b[i][4]} | {b[i][5]} | {b[i][6]} | {b[i][7]} |")
        print(outline)
        pass

    def setup_board(self):
        self.state = np.ndarray((8,8), dtype=Piece)
            #QUESTION from Charlie to Elijah- what is advantage to numpy ndarray? Instead of normal 2d list here
        
        pieces = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]
        for i in range(8):
            #Setting up non-pawn row
            self.state[0][i] = pieces[i](False) #black pieces at the top
            self.state[7][i] = pieces[i](True)  #white pieces at the bottom
                
            #Setting up pawn rows    
            self.state[1][i] = Pawn(False)
            self.state[6][i] = Pawn(True)

            #empty rows, which is rows 2-6
            for j in range(2, 6):
                self.state[j][i] = Empty() 
    
    #this allows us to subscript the Board object
    # so if b = Board(), then b[2] will give row2
    # and therefore b[2][4] will give us tile 2,4
    def __getitem__(self, item):
        return self.state[item]

    
