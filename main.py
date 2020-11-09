"""
    main.py

    Game main file
"""

import pyxel
from random import randint
from math import ceil

from module.object import Moyen_Roc, Object, Grand_Roc, Petit_Roc
from module.player import Player

# Main class
class Game(object):
    def __init__(self):
        pyxel.init(255, 255, caption="MOONSHOT", quit_key=pyxel.KEY_Q, fps=20)
        pyxel.image(0).load(0, 0, "assets/object.png")

        self.list_object = []
        for _ in range(0,5):
            self.list_object.append(Grand_Roc(randint(0, 255), randint(0, 255), 0, 0, 16, 16))
        for _ in range(0,10):
            self.list_object.append(Moyen_Roc(randint(0, 255), randint(0, 255), 72, 24, 16, 8))
        for _ in range(0,20):
            self.list_object.append(Petit_Roc(randint(0, 255), randint(0, 255), 72, 16, 16, 8))

        # Player
        self.player = Player(randint(0, 255), randint(0, 255), 10)

        pyxel.run(self.update, self.draw)

    def draw_player(self, player):
        pyxel.circ(player.x, player.y, 3, 10)

    def draw_heart(self):
        nb_heart = ceil(self.player.life_max/3)
        for i in range(nb_heart):
            if self.player.life>=(i+1)*3:
                pyxel.blt(1+(9*i), 1, 0, 24, 16, 8, 8, 13)
            elif abs(self.player.life-((i+1)*3))>3:
                pyxel.blt(1+(9*i), 1, 0, 48, 16, 8, 8, 13)
            else:
                pyxel.blt(1+(9*i), 1, 0, 48-(8*(3-abs(self.player.life-((i+1)*3)))), 16, 8, 8, 13)

    def update(self):
        list_pyxel = []
        for obj in self.list_object:
            for pyx in obj.list_pyxels:
                list_pyxel.append(pyx)

        if pyxel.btn(pyxel.KEY_K) and [self.player.x-1, self.player.y] not in list_pyxel and self.player.x>0:
            self.player.x = (self.player.x - 1)
        elif pyxel.btn(pyxel.KEY_O) and [self.player.x, self.player.y-1] not in list_pyxel and self.player.y>0:
            self.player.y = (self.player.y - 1) 
        elif pyxel.btn(pyxel.KEY_M) and [self.player.x+1, self.player.y] not in list_pyxel and self.player.x<255:
            self.player.x = (self.player.x + 1)
        elif pyxel.btn(pyxel.KEY_L) and [self.player.x, self.player.y+1] not in list_pyxel and self.player.y<255:
            self.player.y = (self.player.y + 1)

    def draw(self):
        pyxel.cls(1)
        # Map
        for obj in self.list_object:
            pyxel.blt(obj.x, obj.y, 0, obj.u, obj.v, obj.w, obj.h, 13)
        # Player
        self.draw_player(self.player)

        # Life
        self.draw_heart()

# Lancement du jeu
Game()