"""
    player.py : Class Player
"""

# Player class
class Player(object):
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