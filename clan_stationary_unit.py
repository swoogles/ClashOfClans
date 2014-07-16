from clan_unit import Unit
class DefensiveUnit(Unit):
  name = "Abstract DefensiveUnit"

  def __init__(self, level=1):
    super(UnitUnit, self).__init__(level)

  def drawingInfo(self):
    return self.color, (self.pos_3d[0]*10, self.pos_3d[1]*10, self.width*10, self.width*10), self.fill
