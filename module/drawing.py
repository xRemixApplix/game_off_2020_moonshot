import pyxel

from math import ceil

def draw_explosion(x, y):
    """
        Aspect of the explosion
    """
    pyxel.circ(x, y, 5, 14)


def draw_target(x, y):
    """
        Aspect of the mouse pointer
    """
    pyxel.blt(x-4, y-4, 0, 0, 96, 9, 9, 13)


def draw_teleport(x, y, u, v, w, h):
    pyxel.blt(x, y, 0, u, v, w, h, 13)