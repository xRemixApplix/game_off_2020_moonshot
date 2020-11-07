"""
    main.py

    Game main file
"""

import pyxel
from random import randint

from module.object import Object, Roc
from module.player import Player

# Main class
class Game(object):
    def __init__(self):
        pyxel.init(255, 255, caption="MOONSHOT", quit_key=pyxel.KEY_Q, fps=20)
        pyxel.image(0).load(0, 0, "assets/object.png")

        self.list_object = []
        for _ in range(0,10):
            self.list_object.append(Roc(randint(0, 255), randint(0, 255)))

        # Player
        self.player = Player(randint(0, 255), randint(0, 255))

        pyxel.run(self.update, self.draw)

    def draw_player(self, player):
        pyxel.circ(player.x, player.y, 3, 10)

    def update(self):
        list_pyxel = []
        for obj in self.list_object:
            for pyx in obj.list_pyxels:
                list_pyxel.append(pyx)

        if pyxel.btn(pyxel.KEY_K) and [self.player.x-1, self.player.y] not in list_pyxel:
            self.player.x = (self.player.x - 1)
        elif pyxel.btn(pyxel.KEY_O) and [self.player.x, self.player.y-1] not in list_pyxel:
            self.player.y = (self.player.y - 1) 
        elif pyxel.btn(pyxel.KEY_M) and [self.player.x+1, self.player.y] not in list_pyxel:
            self.player.x = (self.player.x + 1)
        elif pyxel.btn(pyxel.KEY_L) and [self.player.x, self.player.y+1] not in list_pyxel:
            self.player.y = (self.player.y + 1)

    def draw(self):
        pyxel.cls(13)
        # Map
        for obj in self.list_object:
            pyxel.blt(obj.x, obj.y, 0, 0, 0, 16, 16, 13)
        # Player
        self.draw_player(self.player)

# Lancement du jeu
Game()