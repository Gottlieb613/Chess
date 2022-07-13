import numpy as np
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
            print(f"| {b[1][i]} | {b[2][i]} | {b[3][i]} | {b[4][i]} | {b[5][i]} | {b[6][i]} | {b[7][i]} | {b[8][i]} |")
        print(outline)
        pass

    def setup_board(self):
        self.state = np.ndarray(size = (8,8))
    
