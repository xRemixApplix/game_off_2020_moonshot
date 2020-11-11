"""
    main.py : Game main file
"""

from random import randint
from math import ceil, sqrt

import pyxel

from module.object import Moyen_Roc, Grand_Roc, Petit_Roc
from module.character import Enemy, Player
from module.projectile import Projectile

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
        # Projectiles
        self.projectiles = []
        self.explosions = []

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

    def draw_projectile(self, projectile):
        pyxel.circ(projectile.x, projectile.y, 1, 7)

    def draw_explosion(self, explosion):
        pyxel.circ(explosion.x, explosion.y, 6, 14)

    def get_distance(self, var_1, var_2):
        return sqrt(abs(var_1.x-var_2.x)**2+abs(var_1.y-var_2.y)**2)

    def get_list_object(self):
        list_pyxel = []
        for obj in self.list_object: list_pyxel += obj.list_pyxels

        return list_pyxel

    def update(self):
        """
            Update function
        """
        list_pyxel = self.get_list_object()
        self.explosions = []
        dx = dy = 0

        # Player's actions
        if pyxel.btn(pyxel.KEY_K) and [self.player.x-1, self.player.y] not in list_pyxel and self.player.x > 0:
            self.player.x = (self.player.x - 1)
            dx = -1
        if pyxel.btn(pyxel.KEY_O) and [self.player.x, self.player.y-1] not in list_pyxel and self.player.y > 0:
            self.player.y = (self.player.y - 1)
            dy = -1
        if pyxel.btn(pyxel.KEY_M) and [self.player.x+1, self.player.y] not in list_pyxel and self.player.x < 255:
            self.player.x = (self.player.x + 1)
            dx = 1
        if pyxel.btn(pyxel.KEY_L) and [self.player.x, self.player.y+1] not in list_pyxel and self.player.y < 255:
            self.player.y = (self.player.y + 1)
            dy = 1

        if pyxel.btnp(pyxel.KEY_SPACE) and (dx != dy):
                self.projectiles.append(Projectile(self.player.x, self.player.y, dx, dy))

        # Enemies movement
        for enemy in self.enemies:
            if 50<self.get_distance(self.player, enemy)<100:
                if abs(self.player.x-enemy.x)>0 and [(enemy.x + ((self.player.x-enemy.x)//abs(self.player.x-enemy.x))), enemy.y] not in list_pyxel:
                    enemy.x = (enemy.x + ((self.player.x-enemy.x)//abs(self.player.x-enemy.x)))
                if abs(self.player.y-enemy.y)>0 and [enemy.x, (enemy.y + ((self.player.y-enemy.y)//abs(self.player.y-enemy.y)))] not in list_pyxel:
                    enemy.y = (enemy.y + ((self.player.y-enemy.y)//abs(self.player.y-enemy.y)))

        # Projectiles explosion
        for projectile in self.projectiles:
            if [projectile.x, projectile.y] in list_pyxel:
                self.explosions.append(projectile)
                self.projectiles.remove(projectile)

            for enemy in self.enemies:
                if self.get_distance(enemy, projectile)<5:
                    self.explosions.append(projectile)
                    self.projectiles.remove(projectile)
                    self.enemies.remove(enemy)

        # Projectiles out of the screen
        for projectile in self.projectiles:
            if 0<projectile.x<255 or 0<projectile.y<255:
                self.projectiles.remove(projectiles)

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
        # Projectiles
        for projectile in self.projectiles:
            projectile.update_position()
            self.draw_projectile(projectile)
        # Explosions
        for explosion in self.explosions:
            self.draw_explosion(explosion)
        # Health bar
        self.draw_heart()

# Game loop
Game()
