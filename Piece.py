

#imports

class Piece():
    def __init__(self, white):
        self.white = white

    #maybe this shuoldn't be in Piece() but in the individual subclasses? since
    # this function should behave differently for the different pieces?
    def is_valid_move(self):
        # TODO
        pass

    #self.white is a boolean
    def isWhite(self):
        return self.white


class Pawn(Piece):
    def __init__(self, white):
        super().__init__(white) #i think this is how you can just use the superclass's initialization

class Rook(Piece):
    def __init__(self):
        pass

class Knight(Piece):
    def __init__(self):
        pass

class Bishop(Piece):
    def __init__(self):
        pass

class Queen(Piece):
    def __init__(self):
        pass

class King(Piece):
    def __init__(self):
        pass
    
class InvisiblePawn(Piece):
    # For en passant
    
    def __init__(self):
        pass


