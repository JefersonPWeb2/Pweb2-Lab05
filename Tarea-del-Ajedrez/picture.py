from colors import color
from colors import inverter

class Picture:
    def __init__(self, img):
        self.img = img

    def __eq__(self, other):
        return self.img == other.img

    def _invColor(self, color):
        if color not in inverter:
            return color
        return inverter[color]

    def verticalMirror(self):
        return Picture(self.img[::-1])

    def horizontalMirror(self):
        horizontal = []
        for row in self.img:
            horizontal.append(row[::-1])
        return Picture(horizontal)

    def negative(self):

        negative = []
        for row in self.img:
            negative_row = [self._invColor(pixel) for pixel in row]
            negative.append(negative_row)
        return Picture(negative)

    def join(self, p):
        joined_img = []
        for i in range(len(self.img)):
            joined_row = ''.join(self.img[i]) + ''.join(p.img[i])
            joined_img.append(joined_row)
        return Picture(joined_img)

    def up(self, p):
        new_img = p.img + self.img
        return Picture(new_img)

    def under(self, p):
        new_img = self.img + p.img
        return Picture(new_img)

    def insert(self, p):
        return Picture(None)

    def horizontalRepeat(self, n):
        repeated_img = [row * n for row in self.img]
        return Picture(repeated_img)

    def verticalRepeat(self, n):
        repeated_img = []
        for _ in range(n):
            repeated_img.extend(self.img)
        return Picture(repeated_img)

    def insert(self, p):
        insert_img = []
        for row_self, row_p in zip(self.img, p.img):
            insert_row = ''.join([c_self if c_self != ' ' else c_p for c_self, c_p in zip(row_self,row_p)])
        return Picture(insert_img)
