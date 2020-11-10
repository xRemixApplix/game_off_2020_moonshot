"""
    main.py : Game main file
"""

from random import randint
from math import ceil, sqrt

import pyxel

from module.object import Moyen_Roc, Grand_Roc, Petit_Roc
from module.character import Enemy, Player

# Main class
class Game(object):
    """
        Game's general class
    """
    def __init__(self):
        pyxel.init(255, 255, caption="MOONSHOT", quit_key=pyxel.KEY_Q, fps=20)
        pyxel.image(0).load(0, 0, "assets/object.png")

        # Object generation with random position
        self.list_object = []
        for _ in range(0, 5):
            self.list_object.append(Grand_Roc(randint(0, 255), randint(0, 255), 0, 0, 16, 16))
        for _ in range(0, 10):
            self.list_object.append(Moyen_Roc(randint(0, 255), randint(0, 255), 72, 24, 16, 8))
        for _ in range(0, 20):
            self.list_object.append(Petit_Roc(randint(0, 255), randint(0, 255), 72, 16, 16, 8))

        # Player
        self.player = Player(randint(0, 255), randint(0, 255), 10)
        # Enemies
        self.enemies = [Enemy(randint(0, 255), randint(0, 255), 10) for _ in range(5)]

        pyxel.run(self.update, self.draw)

    def draw_player(self, player):
        """
            Aspect of the player
        """
        pyxel.circ(player.x, player.y, 3, 10)

    def draw_enemy(self, enemy):
        """
            Aspect of the enemy
        """
        pyxel.circ(enemy.x, enemy.y, 3, 8)

    def draw_heart(self):
        """
            Drawing heart for health bar
        """
        nb_heart = ceil(self.player.life_max/3)
        for i in range(nb_heart):
            # Heart full
            if self.player.life >= (i+1)*3:
                pyxel.blt(1+(9*i), 1, 0, 24, 16, 8, 8, 13)
            # Heart empty
            elif abs(self.player.life-((i+1)*3)) > 3:
                pyxel.blt(1+(9*i), 1, 0, 48, 16, 8, 8, 13)
            # Heart mid
            else:
                pyxel.blt(1+(9*i), 1, 0, 48-(8*(3-abs(self.player.life-((i+1)*3)))), 16, 8, 8, 13)

    def distance(self, player, enemy):
        return sqrt(abs(player.x-enemy.x)**2+abs(player.y-enemy.y)**2)

    def update(self):
        """
            Update function
        """
        list_pyxel = []
        for obj in self.list_object:
            for pyx in obj.list_pyxels:
                list_pyxel.append(pyx)

        # Player's actions
        if pyxel.btn(pyxel.KEY_K) and [self.player.x-1, self.player.y] not in list_pyxel and self.player.x > 0:
            self.player.x = (self.player.x - 1)
        if pyxel.btn(pyxel.KEY_O) and [self.player.x, self.player.y-1] not in list_pyxel and self.player.y > 0:
            self.player.y = (self.player.y - 1)
        if pyxel.btn(pyxel.KEY_M) and [self.player.x+1, self.player.y] not in list_pyxel and self.player.x < 255:
            self.player.x = (self.player.x + 1)
        if pyxel.btn(pyxel.KEY_L) and [self.player.x, self.player.y+1] not in list_pyxel and self.player.y < 255:
            self.player.y = (self.player.y + 1)

        # Enemies movement
        for enemy in self.enemies:
            if 10<self.distance(self.player, enemy)<50:
                if abs(self.player.x-enemy.x)>0 and [(enemy.x + ((self.player.x-enemy.x)//abs(self.player.x-enemy.x))), enemy.y] not in list_pyxel:
                    enemy.x = (enemy.x + ((self.player.x-enemy.x)//abs(self.player.x-enemy.x)))
                if abs(self.player.y-enemy.y)>0 and [enemy.x, (enemy.y + ((self.player.y-enemy.y)//abs(self.player.y-enemy.y)))] not in list_pyxel:
                    enemy.y = (enemy.y + ((self.player.y-enemy.y)//abs(self.player.y-enemy.y)))

    def draw(self):
        """
            Drawing function
        """
        pyxel.cls(1)
        # Map
        for obj in self.list_object:
            pyxel.blt(obj.x, obj.y, 0, obj.u, obj.v, obj.w, obj.h, 13)
        # Player
        self.draw_player(self.player)
        # Enemies
        for enemy in self.enemies:
            self.draw_enemy(enemy)
        # Health bar
        self.draw_heart()

# Game loop
Game()
