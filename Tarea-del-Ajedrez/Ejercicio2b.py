from interpreter import draw
from chessPictures import *

horse = knight
horseN = horse.negative()

horses = horse.join(horseN)
horsesInv = horses.horizontalMirror()

horses4 = horses.under(horsesInv)

draw(horses4)
