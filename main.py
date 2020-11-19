"""
    main.py : Game main file
"""

from random import randint
from math import ceil, sqrt, pi
import os
import json

import pyxel

from module.object import Moyen_Roc, Grand_Roc, Petit_Roc, Orb
from module.character import Enemy, Player
from module.projectile import Projectile

# Main class
class Game(object):
    """
        Game's general class
    """
    def __init__(self):
        pyxel.init(255, 255, caption="MOONSHOT", quit_key=pyxel.KEY_ESCAPE, fps=20)
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
        self.enemies = []
        # Projectiles
        self.projectiles = []
        self.explosions = []
        # Orb
        self.orb = []
        
        if os.path.isfile('resource/statistics.json'):
            with open('resource/statistics.json', 'r') as stats:
                json_stats = json.load(stats)
                self.player.level = int(json_stats["level_player"])
                self.player.life = self.player.life_max = int(json_stats["life_player"])
                self.player.attack = int(json_stats["attack_player"])
                self.player.defense = int(json_stats["defense_player"])
                self.player.speed = int(json_stats["speed_player"])
                self.reward = int(json_stats["reward_points"])
        else:
            self.reward = 0

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
        pyxel.blt(enemy.x-8, enemy.y-8, 0, 0, 105, 16, 15, 13)
        pyxel.text(enemy.x+8, enemy.y-8, "{}".format(enemy.life), 8)

    def draw_orb(self, orb):
        """
            Aspect of the orb
        """
        pyxel.blt(orb.x, orb.y, 0, orb.u, orb.v, orb.w, orb.h, 13)

    def draw_target(self, x, y):
        """
            Aspect of the mouse pointer
        """
        pyxel.blt(x-4, y-4, 0, 0, 96, 9, 9, 13)

    def draw_heart(self):
        """
            Drawing heart for health bar
        """
        nb_heart = ceil(self.player.life_max/3)
        for i in range(nb_heart):
            # Heart full
            if self.player.life >= (i+1)*3:
                pyxel.blt(1+(17*i), 1, 0, 152, 16, 16, 16, 13)
            # Heart empty
            elif abs(self.player.life-((i+1)*3)) > 3:
                pyxel.blt(1+(17*i), 1, 0, 200, 16, 16, 16, 13)
            # Heart mid
            else:
                pyxel.blt(1+(17*i), 1, 0, 200-(16*(3-abs(self.player.life-((i+1)*3)))), 16, 16, 16, 13)

    def draw_projectile(self, projectile):
        pyxel.circ(projectile.x, projectile.y, 1, 7)

    def draw_explosion(self, explosion):
        pyxel.circ(explosion.x, explosion.y, 5, 14)

    def get_distance(self, var_1, var_2):
        return sqrt(abs(var_1.x-var_2.x)**2+abs(var_1.y-var_2.y)**2)

    def get_list_object(self):
        list_pyxel = []
        for obj in self.list_object: list_pyxel += obj.list_pyxels

        return list_pyxel

    def get_list_enemy(self):
        list_pyxel = []
        for enemy in self.enemies: list_pyxel += enemy.get_list_pyxels()

        return list_pyxel

    def get_versus_list_enemies(self, enemy_target):
        enemies_pyxel = []
        for enemy in self.enemies:
            if enemy!=enemy_target: enemies_pyxel += enemy.get_list_pyxels()

        return enemies_pyxel

    def update(self):
        """
            Update function
        """
        list_pyxel = self.get_list_object()
        list_pyxel_enemies = self.get_list_enemy()
        self.explosions = []
        dx = dy = 0

        # Player's actions
        if pyxel.btn(pyxel.KEY_Q) and [self.player.x-1, self.player.y] not in list_pyxel and self.player.x > 0:
            self.player.x = (self.player.x - 1)
        if pyxel.btn(pyxel.KEY_Z) and [self.player.x, self.player.y-1] not in list_pyxel and self.player.y > 0:
            self.player.y = (self.player.y - 1)
        if pyxel.btn(pyxel.KEY_D) and [self.player.x+1, self.player.y] not in list_pyxel and self.player.x < 255:
            self.player.x = (self.player.x + 1)
        if pyxel.btn(pyxel.KEY_S) and [self.player.x, self.player.y+1] not in list_pyxel and self.player.y < 255:
            self.player.y = (self.player.y + 1)

        if pyxel.btnp(pyxel.MOUSE_LEFT_BUTTON) and [pyxel.mouse_x, pyxel.mouse_y] in list_pyxel_enemies: 
            dx = abs(self.player.x-pyxel.mouse_x)/sqrt((self.player.x-pyxel.mouse_x)**2+(self.player.y-pyxel.mouse_y)**2)
            dy = abs(self.player.y-pyxel.mouse_y)/sqrt((self.player.x-pyxel.mouse_x)**2+(self.player.y-pyxel.mouse_y)**2)
            self.projectiles.append(Projectile(self.player.x, self.player.y, dx if self.player.x<pyxel.mouse_x else -dx, dy if self.player.y<pyxel.mouse_y else -dy, 50))

        # Enemies movement
        for enemy in self.enemies:
            if 10<self.get_distance(self.player, enemy)<100:
                if abs(self.player.x-enemy.x)>0 and [(enemy.x + ((self.player.x-enemy.x)//abs(self.player.x-enemy.x))), enemy.y] not in list_pyxel and [(enemy.x + ((self.player.x-enemy.x)//abs(self.player.x-enemy.x))), enemy.y] not in self.get_versus_list_enemies(enemy):
                    enemy.x = (enemy.x + ((self.player.x-enemy.x)//abs(self.player.x-enemy.x)))
                if abs(self.player.y-enemy.y)>0 and [enemy.x, (enemy.y + ((self.player.y-enemy.y)//abs(self.player.y-enemy.y)))] not in list_pyxel and [enemy.x, (enemy.y + ((self.player.y-enemy.y)//abs(self.player.y-enemy.y)))] not in self.get_versus_list_enemies(enemy):
                    enemy.y = (enemy.y + ((self.player.y-enemy.y)//abs(self.player.y-enemy.y)))

        # Projectiles end of run
        for enemy in self.enemies:
            for projectile in self.projectiles:
                if self.get_distance(enemy, projectile)<6:
                    self.explosions.append(projectile)
                    self.projectiles.remove(projectile)
                    enemy.life -= 1
                    if enemy.life<1:
                        if not self.player.orb_find and randint(1, 50) in range(5) and len(self.orb)==0:
                            self.orb.append(Orb(enemy.x, enemy.y, 64, 16, 8, 8))
                            self.player.orb_find = True
                        self.enemies.remove(enemy)
                if projectile.distance>=projectile.scope:
                    self.projectiles.remove(projectile)

        for projectile in self.projectiles:
            if [int(projectile.x), int(projectile.y)] in list_pyxel:
                self.explosions.append(projectile)
                self.projectiles.remove(projectile)

             # Projectiles out of the screen
            if 0>projectile.x>255 or 0>projectile.y>255:
                self.projectiles.remove(projectile)

        if len(self.orb)>0 and [self.player.x, self.player.y] in self.orb[0].list_pyxels:
            self.orb = []
            self.player.orb_find = True
            self.orb.append(Orb(235, 1, 168, 0, 16, 16))

        if len(self.enemies)<1:
            while len(self.enemies) < 5:
                self.enemies.append(Enemy(randint(0, 255), randint(0, 255), 10))

    def draw(self):
        """
            Drawing function
        """
        pyxel.cls(1)
        # Orbs
        pyxel.line(251, 1, 253, 1, 7)
        pyxel.line(253, 1, 253, 17, 7)
        pyxel.line(251, 17, 253, 17, 7)

        pyxel.line(233, 1, 235, 1, 7)
        pyxel.line(233, 1, 233, 17, 7)
        pyxel.line(233, 17, 235, 17, 7)
        if len(self.orb)>0:
            self.draw_orb(self.orb[0])
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
        # Mouse
        self.draw_target(pyxel.mouse_x, pyxel.mouse_y)
# Game loop
Game()
