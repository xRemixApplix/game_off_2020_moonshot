"""
    object.py : Class Object
"""

# Object Class
class Object(object):
    def __init__(self, x, y, u, v, w, h):
        self.__x = x
        self.__y = y
        self.__u = u
        self.__v = v
        self.__w = w
        self.__h = h
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

    @property
    def u(self):
        return self.__u
    @u.setter
    def u(self, value):
        self.__u = value

    @property
    def v(self):
        return self.__v
    @v.setter
    def v(self, value):
        self.__v = value

    @property
    def w(self):
        return self.__w
    @w.setter
    def w(self, value):
        self.__w = value

    @property
    def h(self):
        return self.__h
    @h.setter
    def h(self, value):
        self.__h = value

class Grand_Roc(Object):
    def __init__(self, x, y, u, v, w, h):
        super().__init__(x, y, u, v, w, h)
        self.list_pyxels = self.fill_list_pixels(x, y)

    def fill_list_pixels(self, x, y):
        tab_pyxels = []

        for i in range(10, 13): tab_pyxels.append([x, y+i])
        for i in range(5, 14): tab_pyxels.append([x+1, y+i])
        for i in range(2, 14): tab_pyxels.append([x+2, y+i])
        for i in range(1, 15): tab_pyxels.append([x+3, y+i])
        for i in range(15): tab_pyxels.append([x+4, y+i])
        for i in range(15): tab_pyxels.append([x+5, y+i])
        for i in range(16): tab_pyxels.append([x+6, y+i])
        for i in range(16): tab_pyxels.append([x+7, y+i])
        for i in range(1, 16): tab_pyxels.append([x+8, y+i])
        for i in range(2, 16): tab_pyxels.append([x+9, y+i])
        for i in range(2, 16): tab_pyxels.append([x+10, y+i])
        for i in range(2, 16): tab_pyxels.append([x+11, y+i])
        for i in range(3, 15): tab_pyxels.append([x+12, y+i])
        for i in range(3, 15): tab_pyxels.append([x+13, y+i])
        for i in range(4, 14): tab_pyxels.append([x+14, y+i])
        for i in range(7, 13): tab_pyxels.append([x+15, y+i])

        return tab_pyxels

class Teleport(Object):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 0, 16, 16)

    def activated(self):
        self.u = 0
        self.v = 16

class Moyen_Roc(Object):
    def __init__(self, x, y, u, v, w, h):
        super().__init__(x, y, u, v, w, h)
        self.list_pyxels = self.fill_list_pixels(x, y)

    def fill_list_pixels(self, x, y):
        tab_pyxels = []

        for i in range(4, 6): tab_pyxels.append([x+1, y+i])
        for i in range(3, 6): tab_pyxels.append([x+2, y+i])
        for i in range(3, 7): tab_pyxels.append([x+3, y+i])
        for i in range(1, 8): tab_pyxels.append([x+4, y+i])
        for i in range(8): tab_pyxels.append([x+5, y+i])
        for i in range(7): tab_pyxels.append([x+6, y+i])
        for i in range(7): tab_pyxels.append([x+7, y+i])
        for i in range(7): tab_pyxels.append([x+8, y+i])
        for i in range(7): tab_pyxels.append([x+9, y+i])
        for i in range(7): tab_pyxels.append([x+10, y+i])
        for i in range(7): tab_pyxels.append([x+11, y+i])
        for i in range(7): tab_pyxels.append([x+12, y+i])
        for i in range(1, 6): tab_pyxels.append([x+13, y+i])
        for i in range(2, 6): tab_pyxels.append([x+14, y+i])
        for i in range(3, 6): tab_pyxels.append([x+15, y+i])

        return tab_pyxels

class Petit_Roc(Object):
    def __init__(self, x, y, u, v, w, h):
        super().__init__(x, y, u, v, w, h)
        self.list_pyxels = self.fill_list_pixels(x, y)

    def fill_list_pixels(self, x, y):
        tab_pyxels = []

        for i in range(6): tab_pyxels.append([x+3, y+i])
        for i in range(4, 6): tab_pyxels.append([x+4, y+i])
        for i in range(3, 6): tab_pyxels.append([x+5, y+i])
        for i in range(1, 7): tab_pyxels.append([x+6, y+i])
        for i in range(7): tab_pyxels.append([x+7, y+i])
        for i in range(7): tab_pyxels.append([x+8, y+i])
        for i in range(7): tab_pyxels.append([x+9, y+i])
        for i in range(1, 7): tab_pyxels.append([x+10, y+i])
        for i in range(2, 6): tab_pyxels.append([x+11, y+i])
        for i in range(4, 6): tab_pyxels.append([x+12, y+i])

        return tab_pyxels

class Orb(Object):
    def __init__(self, x, y, u, v, w, h):
        super().__init__(x, y, u, v, w, h)
        self.list_pyxels = self.fill_list_pixels(x, y)

    def fill_list_pixels(self, x, y):
        tab_pyxels = []

        for i in range(2, 6): tab_pyxels.append([x, y+i])
        for i in range(1, 7): tab_pyxels.append([x+1, y+i])
        for i in range(8): tab_pyxels.append([x+2, y+i])
        for i in range(8): tab_pyxels.append([x+3, y+i])
        for i in range(8): tab_pyxels.append([x+4, y+i])
        for i in range(8): tab_pyxels.append([x+5, y+i])
        for i in range(1, 7): tab_pyxels.append([x+6, y+i])
        for i in range(2, 6): tab_pyxels.append([x+7, y+i])

        return tab_pyxels