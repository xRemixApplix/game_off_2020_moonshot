"""
    projectile.py : projectile's Class
"""

class Projectile(object):
    """
        Projectile class
    """
    def __init__(self, x, y, dx, dy):
        self.__x = x
        self.__y = y
        self.__dx = dx
        self.__dy = dy

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
    def dx(self):
        return self.__dx
    @dx.setter
    def dx(self, value):
        self.__dx = value

    @property
    def dy(self):
        return self.__dy
    @dy.setter
    def dy(self, value):
        self.__dy = value

    def update_position(self):
        self.x += self.dx + self.dx
        self.y += self.dy + self.dy