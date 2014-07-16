from clan_unit import Unit
class ActiveUnit(Unit):
  name = "Abstract ActiveUnit"

  def __init__(self, level=1):
    super(ActiveUnit, self).__init__(level)
    self.dps = self._prop_levels_dps[level]
    self.lastAttack = 0.0
    self.attackSpeed = 1.0
    self._target = None

  def attackIfPossible(self, gameTime):
    if ( self.lastAttack + self.attackSpeed < gameTime ):
      self.lastAttack = gameTime
      self.attack()

  def attack(self):
    print("Attack.")
    self._target.hp_cur -= self.dps
    if ( self._target.isAlive() == False ):
      del self._target
      self._target = None

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
    livingUnits = [unit for unit in enemyUnits if unit.hp_cur > 0]
    distanceList = ([ (idx, self.distanceFrom(enemyUnit) ) 
      for idx, enemyUnit in enumerate(livingUnits) ])

    try:
      targetTuple = min(distanceList, key=lambda x: x[1])
      self.setTarget( livingUnits[targetTuple[0]] )
    except ValueError:
      self.setTarget( None )


  def drawingInfo(self):
    return self.color, (int(self.pos_3d[0]), int(self.pos_3d[1])), self.width, self.fill

  def moveUp(self):
    self.pos_3d[1] += 1

  def move(self, moveVec):
    self.pos_3d += moveVec



  def reprJSON(self):
    stats = dict(
        dps=self.dps, 
    )
    parentStats = super(ActiveUnit, self).reprJSON()
    return dict(list(parentStats.items()) + list(stats.items()))

