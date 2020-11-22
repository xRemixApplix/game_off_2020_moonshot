"""
    projectile.py : projectile's Class
"""

class Projectile(object):
    """
        Projectile class
    """
    def __init__(self, x, y, dx, dy, scope, owner, damage):
        self.__x = x
        self.__y = y
        self.__dx = dx
        self.__dy = dy
        self.__scope = scope
        self.__distance = 0
        self.__owner = owner
        self.__damage = damage

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

    @property
    def scope(self):
        return self.__scope
    @scope.setter
    def scope(self, value):
        self.__scope = value

    @property
    def distance(self):
        return self.__distance
    @distance.setter
    def distance(self, value):
        self.__distance = value

    @property
    def owner(self):
        return self.__owner
    @owner.setter
    def owner(self, value):
        self.__owner = value

    @property
    def damage(self):
        return self.__damage
    @damage.setter
    def damage(self, value):
        self.__damage = value

    def update_position(self):
        self.x += self.dx + self.dx
        self.y += self.dy + self.dy
        self.distance += 1

    def max_range(self):
        return self.scope<=self.distance