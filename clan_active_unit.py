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
      self.attack()

  def setTarget(self, target):
    self._target = target

  def getTarget(self):
    return self._target

  def hasTarget(self):
    return hasattr( self, '_target' )

  def acquireTarget(self, enemyUnits):
    distanceList = ([ (idx, self.distanceFrom(enemyUnit) ) 
      for idx, enemyUnit in enumerate(enemyUnits) ])

    targetTuple = min(distanceList, key=lambda x: x[1])
    self.setTarget( enemyUnits[targetTuple[0]] )

  def drawingInfo(self):
    return self.color, (self.pos_3d[0]*10, self.pos_3d[1]*10), self.width*10


  def reprJSON(self):
    stats = dict(
        dps=self.dps, 
    )
    parentStats = super(ActiveUnit, self).reprJSON()
    return dict(list(parentStats.items()) + list(stats.items()))

