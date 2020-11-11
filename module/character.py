"""
    character.py : Character Class
"""

class Character(object):
    """
        Character class
    """
    def __init__(self, x, y, life):
        self.__x = x
        self.__y = y
        self.__life = life
        self.__life_max = life

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
    def life(self):
        return self.__life
    @life.setter
    def life(self, value):
        self.__life = value

    @property
    def life_max(self):
        return self.__life_max
    @life_max.setter
    def life_max(self, value):
        self.__life_max = value


class Player(Character):
    """
        Player class
    """
    def __init__(self, x, y, life):
        super().__init__(x, y, life)


class Enemy(Character):
    """
        Enemy class
    """
    def __init__(self, x, y, life):
        super().__init__(x, y, life)

    def get_list_pyxels(self):
        tab_pyxels = []

        for i in range(-1, 2): tab_pyxels.append([self.x-3, self.y+i])
        for i in range(-2, 3): tab_pyxels.append([self.x-2, self.y+i])
        for i in range(-3, 4): tab_pyxels.append([self.x-1, self.y+i])
        for i in range(-3, 4): tab_pyxels.append([self.x, self.y+i])
        for i in range(-3, 4): tab_pyxels.append([self.x+1, self.y+i])
        for i in range(-2, 3): tab_pyxels.append([self.x+2, self.y+i])
        for i in range(-1, 2): tab_pyxels.append([self.x+3, self.y+i])

        return tab_pyxels