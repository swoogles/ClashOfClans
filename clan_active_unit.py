from clan_unit import Unit
class ActiveUnit(Unit):
  name = "Abstract ActiveUnit"

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

