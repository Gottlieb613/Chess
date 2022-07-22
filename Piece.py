

#imports

class Piece():
    def __init__(self, white):
        self.white = white

    def is_valid_move(self):
        pass

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

    def is_valid_move(self):
        pass #TODO

    def __repr__(self):
        return "P"

class Rook(Piece):
    def __init__(self, white):
        super().__init__(white)

    def is_valid_move(self, board, new_row, new_col):
        pass #TODO

    def __repr__(self):
        return "R"

class Knight(Piece):
    def __init__(self, white):
        super().__init__(white)

    def is_valid_move(self):
        pass #TODO

    def __repr__(self):
        return "N"

class Bishop(Piece):
    def __init__(self, white):
        super().__init__(white)

    def is_valid_move(self):
        pass #TODO


    def __repr__(self):
        return "B"

class Queen(Piece):
    def __init__(self, white):
        super().__init__(white)

    def is_valid_move(self):
        pass #TODO

    def __repr__(self):
        return "Q"

class King(Piece):
    def __init__(self, white):
        super().__init__(white)

    def is_valid_move(self):
        pass #TODO

    def __repr__(self):
        return "K"
    
class InvisiblePawn(Piece):
    # For en passant
    
    def __init__(self, white):
        super().__init__(white)

    #This isnt a real piece so it should never be able to move
    def is_valid_move(self):
        return False

    def __repr__(self):
        return " "
