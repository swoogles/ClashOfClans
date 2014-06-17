from clan_unit import Unit
class ActiveUnit(Unit):
  name = "Abstract ActiveUnit"

  def __init__(self, level=1):
    super(ActiveUnit, self).__init__(level)
    self.dps = self._prop_levels_dps[level]

  def attack(self):
    self._target.hp_cur -= self.dps
    if ( self._target.isAlive() == False ):
      del self._target

  def kill(self):
    while hasattr( self, '_target' ):
      self._target.printHpCur()
      self.attack()

  def setTarget(self, target):
    self._target = target

  def getTarget(self):
    return self._target

  def hasTarget(self):
    return hasattr( self, '_target' )

  def reprJSON(self):
    stats = dict(
        dps=self.dps, 
    )
    parentStats = super(ActiveUnit, self).reprJSON()
    return dict(list(parentStats.items()) + list(stats.items()))

