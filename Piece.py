

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
    
    def __repr__(self):
        pass


class Pawn(Piece):
    def __init__(self, white):
        super().__init__(white) #i think this is how you can just use the superclass's initialization

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
        pass

    def __repr__(self):
        return "B"

class Queen(Piece):
    def __init__(self, white):
        super().__init__(white)
        pass

    def __repr__(self):
        return "Q"

class King(Piece):
    def __init__(self, white):
        super().__init__(white)
        pass

    def __repr__(self):
        return "K"
    
class InvisiblePawn(Piece):
    # For en passant
    
    def __init__(self, white):
        super().__init__(white)
        pass

    def __repr__(self):
        return " "

class Empty(Piece):
    def __init__(self):
        pass

    def __repr__(sefl):
        return " "


