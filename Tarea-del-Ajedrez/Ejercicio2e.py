from interpreter import draw
from chessPictures import *

square2 = square.negative().join(square)
squareF = square2.horizontalRepeat(4)

draw(squareF)
