'''
Disclaimer: I (Charlie) do not know how to do testing in Python
so right now these are just simple tests, and we can change them to be more formal
'''

from Board import *
from Piece import *

b = Board()
b.print_board() #should look like original state of a 
print(not b[1][4].is_white()) #this should be true because that pawn is black
print(b[7][2].is_white()) #should be true because that Bishop is white

#move white pawn up 2
b.move_piece(True, 6, 0, 4, 0)
b.print_board()

#move black pawn down 2
b.move_piece(False, 1, 1, 3, 1)
b.print_board()

#capture black pawn w/ white pawn
b.move_piece(True, 4, 0, 3, 1)
b.print_board()
