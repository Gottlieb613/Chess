

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

    '''Simple function to see if a particular spot on the board
    is a legal 'landing' spot for this piece, i.e. that spot
    is empty or has a piece of the other color
    also obviously it has to be on the board in the first place, so not row=-1 or something
    NOT the same as a 'valid move', which also takes into account
    movement patterns for the pieces
    '''
    def can_land_there(self, board, row, col):
        return board.in_board(row, col) and not self.teammate(board[row][col])

    def valid_move_list(self, board):
        pass

    def is_valid_move(self, board, new_row, new_col):
        return (new_row, new_col) in self.valid_move_list(board)


    #self.white is a boolean
    def isWhite(self):
        if self is None: #for an empty tile
            return None
        return self.white
    
    def teammate(self, piece):
        return self.isWhite() == piece.isWhite()
    
    def opponent(self, piece):
        return self.isWhite() != piece.isWhite()
    
    def __repr__(self):
        if self is None: #for an empty tile
            return " "


class Pawn(Piece):
    def __init__(self, white):
        super().__init__(white)

    '''Works a little different for pawns
    Since they can ONLY go diag if they are capturing
    and can ONLY jump forward if that spot is EMPTY (same w/ double jump)'''
    def valid_move_list(self, board):
        possible_moves = [] # a list of tuples -> (row, col)

        if self.isWhite(): # starts at row6, moves UP (smaller row vals)
            jump1 = self.row - 1
            jump2 = self.row - 2
            can_double_jump = self.row == 6

        else: # black so starts at row 1, moves DOWN (bigger row values)
            jump1 = self.row + 1
            jump2 = self.row + 2
            can_double_jump = self.row == 1
        
        # Single jump up
        if board.in_board(jump1, self.col) and board[jump1, self.col] is None:
            possible_moves.append((jump1, self.col))

        # Double jump
        if can_double_jump and board[jump2, self.col] is None:
            possible_moves.append((jump2, self.col))

        # Diagonal capture
        left = self.col - 1
        right = self.col + 1

        # forward-left
        piece_diag_left = board[jump1][left]
        if board.in_board(jump1, left) and piece_diag_left is not None and self.opponent(piece_diag_left):
            possible_moves.append((jump1, left))
            
        # forward-right
        piece_diag_right = board[jump1][right]
        if board.in_board(jump1, right) and piece_diag_left is not None and self.opponent(piece_diag_right):
            possible_moves.append((jump1, left))

        # en passant 
        
        return possible_moves


    def __repr__(self):
        return "P"


class Rook(Piece):
    def __init__(self, white):
        super().__init__(white)
    
    def valid_move_list(self, board):
        possible_moves = []

        # RIGHT
        for i in range(1, 8):
            new_col = self.col + i

            if not board.in_board(self.row, new_col) or self.teammate(board[self.row][new_col]):
                break

            landing_piece = board[self.row][new_col]
            if landing_piece is None:
                possible_moves.append((self.row, new_col))
            
            if self.opponent(landing_piece):
                possible_moves.append((self.row, new_col))
                break

        # LEFT
        for i in range(1, 8):
            new_col = self.col - i

            if not board.in_board(self.row, new_col) or self.teammate(board[self.row][new_col]):
                break

            landing_piece = board[self.row][new_col]
            if landing_piece is None:
                possible_moves.append((self.row, new_col))
            
            if self.opponent(landing_piece):
                possible_moves.append((self.row, new_col))
                break


        # UP
        for i in range(1, 8):
            new_row = self.row - i

            if not board.in_board(new_row, self.col) or self.teammate(board[new_row][self.col]):
                break

            landing_piece = board[new_row][self.col]
            if landing_piece is None:
                possible_moves.append((new_row, self.col))
            
            if self.opponent(landing_piece):
                possible_moves.append((new_row, self.col))
                break

        # DOWN
        for i in range(1, 8):
            new_row = self.row + i

            if not board.in_board(new_row, self.col) or self.teammate(board[new_row][self.col]):
                break

            landing_piece = board[new_row][self.col]
            if landing_piece is None:
                possible_moves.append((new_row, self.col))
            
            if self.opponent(landing_piece):
                possible_moves.append((new_row, self.col))
                break
        
        return possible_moves

    def __repr__(self):
        return "R"


class Knight(Piece):
    def __init__(self, white):
        super().__init__(white)
    
    def valid_move_list(self, board):
        possible_moves = []

        r = self.row
        c = self.col
        l_shapes = [
            (r-2, c+1), (r-1, c+2), # first quadrant
            (r+1, c-2), (r+2, c-1), # second quadrant
            (r+2, c-1), (r+1, c-2), # third quadrant
            (r-1, c+2), (r-2, c+1), # fourth quadrant
        ]
        
        for move in l_shapes:
            if self.can_land_there(board, move[0], move[1]):
                possible_moves.append(move)
        
        return possible_moves

    def __repr__(self):
        return "N"

class Bishop(Piece):
    def __init__(self, white):
        super().__init__(white)

    def valid_move_list(self, board):
        possible_moves = []

        # UP-RIGHT
        for i in range(1, 8):
            new_row, new_col = self.row - i, self.col + i

            if not board.in_board(new_row, new_col) or self.teammate(board[new_row][new_col]):
                break

            landing_piece = board[new_row][new_col]
            if landing_piece is None:
                possible_moves.append((new_row, new_col))
            
            if self.opponent(landing_piece):
                possible_moves.append((new_row, new_col))
                break

        # UP-LEFT
        for i in range(1, 8):
            new_row, new_col = self.row - i, self.col - i

            if not board.in_board(new_row, new_col) or self.teammate(board[new_row][new_col]):
                break

            landing_piece = board[new_row][new_col]
            if landing_piece is None:
                possible_moves.append((new_row, new_col))
            
            if self.opponent(landing_piece):
                possible_moves.append((new_row, new_col))
                break


        # DOWN-RIGHT
        for i in range(1, 8):
            new_row, new_col = self.row + i, self.col - i

            if not board.in_board(new_row, new_col) or self.teammate(board[new_row][new_col]):
                break

            landing_piece = board[new_row][new_col]
            if landing_piece is None:
                possible_moves.append((new_row, new_col))
            
            if self.opponent(landing_piece):
                possible_moves.append((new_row, new_col))
                break
            
        # DOWN-LEFT
        for i in range(1, 8):
            new_row, new_col = self.row + i, self.col + i

            if not board.in_board(new_row, new_col) or self.teammate(board[new_row][new_col]):
                break

            landing_piece = board[new_row][new_col]
            if landing_piece is None:
                possible_moves.append((new_row, new_col))
            
            if self.opponent(landing_piece):
                possible_moves.append((new_row, new_col))
                break
    
        return possible_moves

    def __repr__(self):
        return "B"


class Queen(Piece):
    def __init__(self, white):
        super().__init__(white)

    def valid_move_list(self, board):
        # A queen's valid moves is exactly a rook + a bishop

        # make a fake Rook object placed the same tile
        # so we can see what a rook's valid_move_list would be
        imitate_rook = Rook(self.white)
        imitate_rook.row = self.row
        imitate_rook.col = self.col
        rook_possible_moves = imitate_rook.valid_move_list(board)

        # same as above but with bishop
        imitate_bishop = Bishop(self.white)
        imitate_bishop.row = self.row
        imitate_bishop.col = self.col
        bishop_possible_moves = imitate_bishop.valid_move_list(board)

        # concatenate the rook and bishop's valid moves
        possible_moves = rook_possible_moves.extend(bishop_possible_moves)
        return possible_moves

    def __repr__(self):
        return "Q"

class King(Piece):
    def __init__(self, white):
        super().__init__(white)
    
    def valid_move_list(self, board):
        possible_moves = []

        r = self.row
        c = self.col
        all_directions = [
            (r-1, c+1), (r-1, c), # ↗, ↑ 
            (r-1, c-1), (r, c-1), # ↖, ←
            (r+1, c-1), (r+1, c), # ↙, ↓ 
            (r+1, c+1), (r, c+1), # ↘, → 
        ]

        for move in all_directions:
            if board.in_board(move[0], move[1]) and not self.teammate(board[move[0]][move[1]]):
                possible_moves.append(move)
            
        return possible_moves

        # TODO: Important. We still need to add a way to remove moves
        # that would put the King in check. Maybe this is done
        # in the actual gameplay loop
        # We could compile a list of the possible next moves for the foe
        # and then use that list to also check for the king
        # we also need to add in 


    def __repr__(self):
        return "K"
    
class InvisiblePawn(Piece):
    # For en passant
    
    def __init__(self, white):
        super().__init__(white)

    # This isnt a real piece so it should never be able to move
    def valid_move_list(self, board):
        return []

    def is_valid_move(self):
        return False

    def __repr__(self):
        return " "