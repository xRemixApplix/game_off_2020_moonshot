"""
    object.py : Class Object
"""

# Object Class
class Object(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.list_pyxels = []
        
    @property
    def x(self):
        return self.__x
    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y
    @y.setter
    def y(self, value):
        self.__y = value


class Roc(Object):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.list_pyxels = self.fill_list_pixels(x, y)
    
    def fill_list_pixels(self, x, y):
        tab_pyxels = []
        tab_pyxels.append([x, y+10])
        tab_pyxels.append([x, y+11])
        tab_pyxels.append([x, y+12])
        
        tab_pyxels.append([x+1, y+5])
        tab_pyxels.append([x+1, y+6])
        tab_pyxels.append([x+1, y+7])
        tab_pyxels.append([x+1, y+8])
        tab_pyxels.append([x+1, y+9])
        tab_pyxels.append([x+1, y+13])

        tab_pyxels.append([x+2, y+2])
        tab_pyxels.append([x+2, y+3])
        tab_pyxels.append([x+2, y+4])
        tab_pyxels.append([x+2, y+13])

        tab_pyxels.append([x+3, y+1])
        tab_pyxels.append([x+3, y+14])

        tab_pyxels.append([x+4, y])
        tab_pyxels.append([x+4, y+14])

        tab_pyxels.append([x+5, y])
        tab_pyxels.append([x+5, y+14])

        tab_pyxels.append([x+6, y])
        tab_pyxels.append([x+6, y+15])

        tab_pyxels.append([x+7, y])
        tab_pyxels.append([x+7, y+15])

        tab_pyxels.append([x+8, y+1])
        tab_pyxels.append([x+8, y+15])

        tab_pyxels.append([x+9, y+2])
        tab_pyxels.append([x+9, y+15])

        tab_pyxels.append([x+10, y+2])
        tab_pyxels.append([x+10, y+15])

        tab_pyxels.append([x+11, y+2])
        tab_pyxels.append([x+11, y+15])

        tab_pyxels.append([x+12, y+3])
        tab_pyxels.append([x+12, y+14])

        tab_pyxels.append([x+13, y+3])
        tab_pyxels.append([x+13, y+14])

        tab_pyxels.append([x+14, y+4])
        tab_pyxels.append([x+14, y+5])
        tab_pyxels.append([x+14, y+6])
        tab_pyxels.append([x+14, y+13])

        tab_pyxels.append([x+15, y+7])
        tab_pyxels.append([x+15, y+8])
        tab_pyxels.append([x+15, y+9])
        tab_pyxels.append([x+15, y+10])
        tab_pyxels.append([x+15, y+11])
        tab_pyxels.append([x+15, y+12])

        return tab_pyxels