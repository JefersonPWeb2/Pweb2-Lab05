from interpreter import draw
from chessPictures import *

square2 = square.join(square.negative())
squareF = square2.horizontalRepeat(4)
squareFinv = squareF.horizontalMirror()
tablero1 = squareF.under(squareFinv)
tablero2 = tablero1.verticalRepeat(2)

b1 = rock.join(knight.join(bishop).join(queen.join(king.join(bishop.join(knight.join(rock))))))
b2 = pawn.horizontalRepeat(8)

b3 = b1.negative().under(b2.negative())
b3 = b3.insert(tablero1)
b4 = b2.under(b1)
b4 = b4.insert(tablero1.horizontalMirror())

b5 = b3.under(tablero2)
b5 = b5.under(b4.horizontalMirror())
draw(b5)