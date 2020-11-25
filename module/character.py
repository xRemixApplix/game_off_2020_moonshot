"""
    character.py : Character Class
"""

import pyxel

class Character(object):
    """
        Character class
    """
    def __init__(self, x, y, life, level, damage):
        self.__x = x
        self.__y = y
        self.__life = life
        self.__life_max = life
        self.__level = level;
        self.__damage = damage;

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
    def damage(self):
        return self.__damage
    @damage.setter
    def damage(self, value):
        self.__damage = value

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
    def __init__(self, x, y, life, level, damage, reward):
        super().__init__(x, y, life, level, damage)
        self.__orb_find = False
        self.__reward = reward

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

    def draw(self):
        """
            Aspect of the player
        """
        pyxel.circ(self.x, self.y, 3, 10)

    def draw_life(self):
        length = self.life/(self.life_max/80)

        pyxel.rect(1, 5, length, 5, 11)

    def draw_exp(self):
        pyxel.text(1, 13, 'TEST', 0)

class Enemy(Character):
    """
        Enemy class
    """
    def __init__(self, x, y, life, level, damage):
        super().__init__(x, y, life, level, damage)

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

    def draw(self):
        """
            Aspect of the enemy
        """
        pyxel.blt(self.x-8, self.y-8, 0, 0, 105, 16, 15, 13)
        # Life bar
        length = self.life/(self.life_max/16)

        pyxel.rect(self.x-9, self.y-9, length, 2, 8)
