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
        self.__level = 0;
        self.__attack = 1;
        self.__defense = 1;
        self._speed = 1;

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

    @property
    def attack(self):
        return self.__attack
    @attack.setter
    def attack(self, value):
        self.__attack = value

    @property
    def defense(self):
        return self.__defense
    @defense.setter
    def defense(self, value):
        self.__defense = value

    @property
    def speed(self):
        return self.__speed
    @speed.setter
    def speed(self, value):
        self.__speed = value

    @property
    def level(self):
        return self.__level
    @level.setter
    def level(self, value):
        self.__level = value


class Player(Character):
    """
        Player class
    """
    def __init__(self, x, y, life):
        super().__init__(x, y, life)
        self.__orb_find = False
        self.__reward = 0

    @property
    def orb_find(self):
        return self.__orb_find
    @orb_find.setter
    def orb_find(self, value):
        self.__orb_find = value

    @property
    def reward(self):
        return self.__reward
    @reward.setter
    def reward(self, value):
        self.__reward = value


class Enemy(Character):
    """
        Enemy class
    """
    def __init__(self, x, y, life):
        super().__init__(x, y, life)

    def get_list_pyxels(self):
        tab_pyxels = []

        for i in range(-2, 0): tab_pyxels.append([self.x-7, self.y+i])
        for i in range(-2, 2): tab_pyxels.append([self.x-6, self.y+i])
        for i in range(-2, 4): tab_pyxels.append([self.x-5, self.y+i])
        for i in range(-2, 3): tab_pyxels.append([self.x-4, self.y+i])
        for i in range(-3, 3): tab_pyxels.append([self.x-3, self.y+i])
        for i in range(-4, 4): tab_pyxels.append([self.x-2, self.y+i])
        for i in range(-4, 5): tab_pyxels.append([self.x-1, self.y+i])
        for i in range(-4, 5): tab_pyxels.append([self.x, self.y+i])
        for i in range(-4, 4): tab_pyxels.append([self.x+1, self.y+i])
        for i in range(-3, 3): tab_pyxels.append([self.x+2, self.y+i])
        for i in range(-2, 3): tab_pyxels.append([self.x+3, self.y+i])
        for i in range(-2, 4): tab_pyxels.append([self.x+4, self.y+i])
        for i in range(-2, 2): tab_pyxels.append([self.x+5, self.y+i])
        for i in range(-2, 0): tab_pyxels.append([self.x+6, self.y+i])

        return tab_pyxels