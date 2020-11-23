"""
    main.py : Game main file
"""

from os import stat
from random import randint, uniform
from math import sqrt, pi
import os
import json

import pyxel

from module.object import Moyen_Roc, Grand_Roc, Petit_Roc, Orb, Teleport
from module.character import Enemy, Player
from module.projectile import Projectile
from module.drawing import draw_player, draw_enemy, draw_orb, draw_target, draw_heart, draw_projectile, draw_explosion, draw_object, draw_teleport

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
        self.enemies_level = 1

        # Projectiles
        self.projectiles = []
        self.explosions = []

        # Orb
        self.orb = []

        # Teleport
        self.teleport = Teleport(randint(0, 255), randint(0, 255))
        
        # Read File informations
        self.stats = {}
        with open('resource/statistics.json', 'r') as stats:
            json_stats = json.load(stats)
            self.stats["level_player"] = int(json_stats["level_player"])
            self.stats["life"] = int(((self.stats["level_player"]/10)+(self.stats["level_player"]/2)+(self.stats["level_player"]*10))*json_stats["bonus_life"])
            self.stats["bonus_life"] = json_stats["bonus_life"]
            self.stats["damage"] = int((((self.stats["level_player"]*50)/10)+(self.stats["level_player"]/2)-(self.stats["level_player"]/5))*json_stats["bonus_attack"])
            self.stats["bonus_attack"] =json_stats["bonus_attack"]
            self.stats["bonus_defense"] =json_stats["bonus_defense"]
            self.stats["bonus_range"] =json_stats["bonus_range"]
            self.stats["experience"] = int(json_stats["experience"])

        # Player
        self.player = Player(randint(0, 255), randint(0, 255), self.stats["life"], self.stats["level_player"], self.stats["damage"], self.stats["experience"])

        self.in_game = True
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
            self.projectiles.append(Projectile(self.player.x, self.player.y, dx if self.player.x<pyxel.mouse_x else -dx, dy if self.player.y<pyxel.mouse_y else -dy, 30, "player", self.player.damage))

        # Enemies movement and shoot
        for enemy in self.enemies:
            # Movement
            if 30<self.get_distance(self.player, enemy)<100:
                if abs(self.player.x-enemy.x)>0 and [(enemy.x + ((self.player.x-enemy.x)//abs(self.player.x-enemy.x))), enemy.y] not in list_pyxel and [(enemy.x + ((self.player.x-enemy.x)//abs(self.player.x-enemy.x))), enemy.y] not in self.get_versus_list_enemies(enemy):
                    enemy.x = (enemy.x + ((self.player.x-enemy.x)//abs(self.player.x-enemy.x)))
                if abs(self.player.y-enemy.y)>0 and [enemy.x, (enemy.y + ((self.player.y-enemy.y)//abs(self.player.y-enemy.y)))] not in list_pyxel and [enemy.x, (enemy.y + ((self.player.y-enemy.y)//abs(self.player.y-enemy.y)))] not in self.get_versus_list_enemies(enemy):
                    enemy.y = (enemy.y + ((self.player.y-enemy.y)//abs(self.player.y-enemy.y)))

            # Shoot
            if self.get_distance(self.player, enemy)<50 and randint(1, 50) in range(5):
                dx = abs(self.player.x-enemy.x)/sqrt((self.player.x-enemy.x)**2+(self.player.y-enemy.y)**2)
                dy = abs(self.player.y-enemy.y)/sqrt((self.player.x-enemy.x)**2+(self.player.y-enemy.y)**2)
                self.projectiles.append(Projectile(enemy.x, enemy.y, dx if enemy.x<self.player.x else -dx, dy if enemy.y<self.player.y else -dy, 30, "enemy", enemy.damage))
        
        # Projectiles end of run
        for enemy in self.enemies:
            for projectile in self.projectiles:
                if self.get_distance(enemy, projectile)<6 and projectile.owner=="player":
                    self.explosions.append(projectile)
                    self.projectiles.remove(projectile)
                    enemy.life -= projectile.damage
                    if enemy.life<=0:
                        if not self.player.orb_find and randint(1, 50) in range(5) and len(self.orb)==0:
                            self.orb.append(Orb(enemy.x, enemy.y, 64, 16, 8, 8))
                        self.enemies.remove(enemy)
                
                # Max range disappear
                if projectile.max_range(): self.projectiles.remove(projectile)

        for projectile in self.projectiles:
            if self.get_distance(self.player, projectile)<4 and projectile.owner=="enemy":
                self.explosions.append(projectile)
                self.projectiles.remove(projectile)
                self.player.life -= projectile.damage

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
            self.teleport.activated()
            self.orb.append(Orb(235, 1, 168, 0, 16, 16))

        # Enemies generation
        if len(self.enemies)<1:
            while len(self.enemies) < 5:
                enemy_life = int(((self.enemies_level/10)+(self.enemies_level/2)+(self.enemies_level*10))*uniform(0.8, 1.2))
                enemy_damage = int((((self.enemies_level*50)/10)+(self.enemies_level/2)-(self.enemies_level/5))*uniform(0.8, 1.2))
                self.enemies.append(Enemy(randint(0, 255), randint(0, 255), enemy_life, self.enemies_level, enemy_damage))

        # End game detection
        if self.player.life <= 0 and self.in_game:
            self.in_game = False
            # Write infos in file statistics.json
            with open('resource/statistics.json', 'w') as stats_file:
                json.dump(self.stats, stats_file, indent=4)


    def draw(self):
        """
            Drawing function
        """
        pyxel.cls(1)

        if self.in_game:
            # Teleport
            draw_teleport(self.teleport.x, self.teleport.y, self.teleport.u, self.teleport.v, self.teleport.w, self.teleport.h)

            # Map
            for obj in self.list_object: draw_object(obj.x, obj.y, obj.u, obj.v, obj.w, obj.h)

            # Player
            draw_player(self.player.x, self.player.y)

            # Enemies
            for enemy in self.enemies: draw_enemy(enemy.x, enemy.y, enemy.life, enemy.life_max)

            # Projectiles
            for projectile in self.projectiles:
                projectile.update_position()
                draw_projectile(projectile.x, projectile.y, projectile.owner)

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
        
        else:
            pyxel.text(110, 122, "GAME OVER", pyxel.frame_count % 16)

        # Mouse
        draw_target(pyxel.mouse_x, pyxel.mouse_y)

# Game loop
Game()
