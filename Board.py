from sqlite3 import Row
import numpy as np
from Piece import *
# I was thinking we would have an object for the board itself
# and maybe some for pieces and the gameplay and then the GUI. idk we'll figure it out

#Note: 
# for now, white is always on bottom, black always on top
# this is pretty much only technically relevant for determining a pawn's movement

class Board:
    state = None 
    
    def __init__(self):
        self.setup_board()
        pass

    def print_board(self):
        b = self.state

        #Key: uppercase is WHITE (start at bottom); lowercase is black (start at top)
        # {
        #         1: ['r', 'n', 'b', 'k', 'q', 'b', 'n', 'r'],
        #         2: ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
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

            #needed to do this little loop so empty tiles, which are Nones, are represented as " " instead of "None"
            r = [b[i][0], b[i][1], b[i][2], b[i][3], b[i][4], b[i][5], b[i][6], b[i][7]]
            for i in range(len(r)):
                if r[i] is None:
                    r[i] = " "

            print(f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]} | {r[5]} | {r[6]} | {r[7]} |")
        print(outline)
        pass

    def setup_board(self):
        self.state = np.ndarray((8,8), dtype=Piece)
            #QUESTION from Charlie to Elijah- what is advantage to numpy ndarray? Instead of normal 2d list here
        
        pieces = [Rook, Knight, Bishop, King, Queen, Bishop, Knight, Rook]
        for i in range(8):
            #Setting up non-pawn row
            self.state[0][i] = pieces[i](False, 0, i) #black pieces at the top
            self.state[7][i] = pieces[i](True, 7, i)  #white pieces at the bottom
                
            #Setting up pawn rows    
            self.state[1][i] = Pawn(False, 1, i)
            self.state[6][i] = Pawn(True, 6, i)

    #this allows us to subscript the Board object
    # so if b = Board(), then b[2] will give row2
    # and therefore b[2][4] will give us tile 2,4
    def __getitem__(self, item):
        return self.state[item]
    
    def in_board(self, row, col):
        return 0 <= row <= 7 and 0 <= col <= 7
    
    #might be interesting to split this into two functions
    # 1 to see if a piece CAN move to another spot
    # and 2 to actually do the moving + capturing
    def move_piece(self, player_white, start_row, start_col, end_row, end_col):
        this_piece = self[start_row][start_col]

        #All errors
        if not self.in_board(start_row, start_col):
            print("Starting coordinates not on board")
        if not self.in_board(end_row, end_col):
            print("Ending coordinates not in board")
        if this_piece is None:
            print("Empty tile chosen")
        if this_piece.is_white() != player_white:
            print("Opponent piece chosen")
        
        print(f"You chose a {this_piece.__repr__()}")
        
        valid_moves = this_piece.valid_move_list(self)
        print(f"valid move list: {valid_moves}")

        if (end_row, end_col) in valid_moves:
            end_piece = self[end_row][end_col]

            #move piece in Board, update Piece.row and .col
            self[end_row][end_col] = this_piece
            this_piece.row = end_row
            this_piece.col = end_col
        
            print("Moved the piece")
            
            #remove that piece from original spot
            self[start_row][start_col] = None

            if this_piece.opponent(end_piece):
                print(f"Captured the opponent's {end_piece.__repr__()}")
                #end_piece still thinks it's at end_row,end_col coordinates but I think
                # that isn't much of a problem, bc board doesn't recognize it
                #**TODO: we may want to include a list of 'captured' pieces
                # in which case we would add end_piece to that list now
        else:
            print("The piece cannot move there")
                
            

            

            
            

        

    
