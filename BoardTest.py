'''
Disclaimer: I (Charlie) do not know how to do testing in Python
so right now these are just simple tests, and we can change them to be more formal
'''

from Board import *
from Piece import *

b = Board()
b.print_board() #should look like original state of a 
print(not b[1][4].isWhite()) #this should be true because that pawn is black
print(b[7][2].isWhite()) #should be true because that Bishop is white
