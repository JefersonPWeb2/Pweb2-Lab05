from interpreter import draw
from chessPictures import *

square2 = square.join(square.negative())
squareF = square2.horizontalRepeat(4)
squareFinv = squareF.horizontalMirror()
square4 = squareF.under(squareFinv).verticalRepeat(2)

draw(square4)
