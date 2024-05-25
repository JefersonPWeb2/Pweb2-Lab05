from interpreter import draw
from chessPictures import *

square2 = square.join(square.negative())
squareF = square2.horizontalRepeat(4)

draw(squareF)
