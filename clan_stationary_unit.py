from clan_unit import Unit


class DefensiveUnit(Unit):
    name = "Abstract DefensiveUnit"

    def __init__(self, level=1):
        super().__init__(level)

    def drawing_info(self):
        return self.color, (self.pos_3d[0] * 10, self.pos_3d[1] * 10, self.width * 10, self.width * 10), self.fill
