"""
    main.py : Game main file
"""

from random import randint
from math import sqrt, pi
import os
import json

import pyxel

from module.object import Moyen_Roc, Grand_Roc, Petit_Roc, Orb
from module.character import Enemy, Player
from module.projectile import Projectile
from module.drawing import draw_player, draw_enemy, draw_orb, draw_target, draw_heart, draw_projectile, draw_explosion, draw_object

# Main class
class Game(object):
    """
        Game's general class
    """
    def __init__(self):
        pyxel.init(255, 255, caption="MOONSHOT", quit_key=pyxel.KEY_ESCAPE, fps=20)
        pyxel.image(0).load(0, 0, "assets/object.png")

        # Objects generation with random position
        self.list_object = []
        for _ in range(0, 20): self.list_object.append(Petit_Roc(randint(0, 255), randint(0, 255), 72, 16, 16, 8))
        for _ in range(0, 10): self.list_object.append(Moyen_Roc(randint(0, 255), randint(0, 255), 72, 24, 16, 8))
        for _ in range(0, 5): self.list_object.append(Grand_Roc(randint(0, 255), randint(0, 255), 0, 0, 16, 16))

        # Enemies
        self.enemies = []

        # Projectiles
        self.projectiles = []
        self.explosions = []

        # Orb
        self.orb = []
        
        # Read File informations
        with open('resource/statistics.json', 'r') as stats:
            json_stats = json.load(stats)

            level = int(json_stats["level_player"])
            life = int(((level/10)+(level/2)+(level*10))*json_stats["bonus_life"])
            damage = int((((level*50)/10)+(level/2)-(level/5))*json_stats["bonus_attack"])
            reward = int(json_stats["reward_points"])

            # Player
            self.player = Player(randint(0, 255), randint(0, 255), life, level, damage, reward)

        pyxel.run(self.update, self.draw)

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
            self.projectiles.append(Projectile(self.player.x, self.player.y, dx if self.player.x<pyxel.mouse_x else -dx, dy if self.player.y<pyxel.mouse_y else -dy, 30))

        # Enemies movement
        for enemy in self.enemies:
            if 15<self.get_distance(self.player, enemy)<100:
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
                    if enemy.life<=0:
                        if not self.player.orb_find and randint(1, 50) in range(5) and len(self.orb)==0:
                            self.orb.append(Orb(enemy.x, enemy.y, 64, 16, 8, 8))
                            self.player.orb_find = True
                        self.enemies.remove(enemy)
                
                # Max range disappear
                if projectile.max_range(): self.projectiles.remove(projectile)

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
            while len(self.enemies) < 5: self.enemies.append(Enemy(randint(0, 255), randint(0, 255), 10, 1, 5))

    def draw(self):
        """
            Drawing function
        """
        pyxel.cls(1)
        # Map
        for obj in self.list_object: draw_object(obj.x, obj.y, obj.u, obj.v, obj.w, obj.h)

        # Player
        draw_player(self.player.x, self.player.y)

        # Enemies
        for enemy in self.enemies: draw_enemy(enemy.x, enemy.y, enemy.life)

        # Projectiles
        for projectile in self.projectiles:
            projectile.update_position()
            draw_projectile(projectile.x, projectile.y)

        # Explosions
        for explosion in self.explosions: draw_explosion(explosion.x, explosion.y)

        # Health bar
        draw_heart(self.player.life_max, self.player.life)

        # Orbs
        pyxel.line(251, 1, 253, 1, 7)
        pyxel.line(253, 1, 253, 17, 7)
        pyxel.line(251, 17, 253, 17, 7)

        pyxel.line(233, 1, 235, 1, 7)
        pyxel.line(233, 1, 233, 17, 7)
        pyxel.line(233, 17, 235, 17, 7)
        if len(self.orb)>0: draw_orb(self.orb[0].x, self.orb[0].y, self.orb[0].u, self.orb[0].v, self.orb[0].w, self.orb[0].h)
            
        # Mouse
        draw_target(pyxel.mouse_x, pyxel.mouse_y)

# Game loop
Game()
