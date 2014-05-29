import random
class Battle:
  _units = []

  _attacking_units_queued = []
  _attacking_units_deployed = []
  _defending_units = []

  def addAttackingUnit(self, newUnit):
    self._attacking_units_queued.append( newUnit )

  def numAttackingUnits(self):
    return len(self._attacking_units_queued) + len(self._attacking_units_deployed)

  def addDefendingUnit(self, newUnit):
    self._defending_units.append( newUnit )

  def numDefendingUnits(self):
    return len(self._defending_units)

  def step(self):
    for curAttacker in self._attacking_units_deployed:
      findTarget(curAttacker, self._defending_units)

  def deployAttackingUnit(self, targetUnitIdx):
    self._attacking_units_deployed.append( self._attacking_units_queued.pop(targetUnitIdx) )


def findTarget(attacker, targets):
  attacker.setTarget( random.choice(targets) )
  