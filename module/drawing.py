import pyxel

from math import ceil


def draw_enemy(x, y, life, life_max):
    """
        Aspect of the enemy
    """
    pyxel.blt(x-8, y-8, 0, 0, 105, 16, 15, 13)
    # Life bar
    length = life/(life_max/16)
    
    pyxel.line(x-9, y-9, (x-8)+length, y-9, 7)
    pyxel.line(x-8, y-8, (x-8)+length, y-8, 7)


def draw_explosion(x, y):
    """
        Aspect of the explosion
    """
    pyxel.circ(x, y, 5, 14)


def draw_heart(life_max, life):
    """
        Drawing heart for health bar
    """
    nb_heart = ceil(life_max/3)
    for i in range(nb_heart):
        # Heart full
        if life >= (i+1)*3:
            pyxel.blt(1+(9*i), 1, 0, 24, 16, 8, 8, 13)
        # Heart empty
        elif abs(life-((i+1)*3)) > 3:
            pyxel.blt(1+(9*i), 1, 0, 48, 16, 8, 8, 13)
        # Heart mid
        else:
            pyxel.blt(1+(9*i), 1, 0, 48-(8*(3-abs(life-((i+1)*3)))), 16, 8, 8, 13)


def draw_object(x, y, u, v, w, h):
    """
        Aspect of the object
    """
    pyxel.blt(x, y, 0, u, v, w, h, 13)


def draw_orb(x, y, u, v, w, h):
    """
        Aspect of the orb
    """
    pyxel.blt(x, y, 0, u, v, w, h, 13)
    

def draw_player(x, y):
    """
        Aspect of the player
    """
    pyxel.circ(x, y, 3, 10)


def draw_projectile(x, y, owner):
    """
        Aspect of the projectile
    """
    if owner=="player":
        pyxel.circ(x, y, 1, 7)
    else:
        pyxel.circ(x, y, 1, 11)


def draw_target(x, y):
    """
        Aspect of the mouse pointer
    """
    pyxel.blt(x-4, y-4, 0, 0, 96, 9, 9, 13)


def draw_teleport(x, y, u, v, w, h):
    pyxel.blt(x, y, 0, u, v, w, h, 13)