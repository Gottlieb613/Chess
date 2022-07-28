

class Piece():
    def __init__(self, white, row, col):
        self.white = white
        #Haven't decided whether or not each Piece
        # should store its own location, even though
        # it's on the Board, to make is_valid_move easier.
        # it might not be necessary, since we can just put
        # the current pos as an argument into is_valid_move each time
        self.row = row
        self.col = col

    #simple function to see if a particular spot on the board
    # is a legal 'landing' spot for this piece, i.e. that spot
    # is empty or has a piece of the other color
    # also obviously it has to be on the board in the first place, so not row=-1 or something
    #NOT the same as a 'valid move', which also takes into account
    # movement patterns for the pieces
    def can_land_there(self, board, row, col):
        if not board.in_board(row, col):
            return False
        return board[row][col] is None or (board[row][col].isWhite() != self.isWhite())

    def valid_move_list(self, board):
        pass

    def is_valid_move(self, board, new_row, new_col):
        return (new_row, new_col) in self.valid_move_list(board)


    #self.white is a boolean
    def isWhite(self):
        if self is None: #for an empty tile
            return None
        return self.white
    
    def __repr__(self):
        if self is None: #for an empty tile
            return " "


class Pawn(Piece):
    def __init__(self, white):
        super().__init__(white)

    def valid_move_list(self, board):
        #TODO: finish!!

        if self.isWhite(): #starts at row6, moves UP (smaller row vals)
            can_double_jump = self.row == 6
        
        else: #black so starts at row 1, moves DOWN (bigger row values)
            can_double_jump = self.row == 1

    def is_valid_move(self):
        pass #TODO

    def __repr__(self):
        return "P"

class Rook(Piece):
    def __init__(self, white):
        super().__init__(white)

    def __repr__(self):
        return "R"

class Knight(Piece):
    def __init__(self, white):
        super().__init__(white)

    def __repr__(self):
        return "N"

class Bishop(Piece):
    def __init__(self, white):
        super().__init__(white)

    def __repr__(self):
        return "B"

class Queen(Piece):
    def __init__(self, white):
        super().__init__(white)

    def __repr__(self):
        return "Q"

class King(Piece):
    def __init__(self, white):
        super().__init__(white)

    def __repr__(self):
        return "K"
    
class InvisiblePawn(Piece):
    # For en passant
    
    def __init__(self, white):
        super().__init__(white)

    #This isnt a real piece so it should never be able to move
    def valid_move_list(self, board):
        return []

    def is_valid_move(self):
        return False

    def __repr__(self):
        return " "