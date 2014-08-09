from clan_unit import Unit


class Structure(Unit):
    name = "Abstract Structure"

    def __init__(self, level=1):
        super(Structure, self).__init__(level)

    def drawing_info(self):
        return self.color, (self.pos_3d[0], self.pos_3d[1], self.width, self.width), self.fill

class Wall(Structure):
    def __init__(self, level=1):
        super(Wall, self).__init__(level)
        self.width = 1

class Barracks(object):
    _prop_levels_capacity = {}
    _prop_levels_capacity[4] = 35
    _prop_levels_capacity[5] = 40
    _prop_levels_capacity[6] = 45

    def __init__(self, level=1):
        self.capacity = self._prop_levels_capacity[level]
        self.level = level

