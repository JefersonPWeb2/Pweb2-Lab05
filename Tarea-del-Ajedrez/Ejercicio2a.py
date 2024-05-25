from interpreter import draw
from chessPictures import *

horse = knight
horseN = horse.negative()
horses = horse.join(horseN)

horsesN = horses.negative()
horses4 = horses.under(horsesN)

draw(horses4)
