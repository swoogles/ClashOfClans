# class ArmyPlanner():
#   """
#   Want to explore some functions that would allow me to easily build armies in this damn game
#   """

class Barracks():
  _prop_levels_capacity = {}
  # _prop_levels_capacity[1] =
  # _prop_levels_capacity[2] =
  # _prop_levels_capacity[3] =
  _prop_levels_capacity[4] = 35
  _prop_levels_capacity[5] = 40
  _prop_levels_capacity[6] = 45

  def __init__(self, level=1):
    self.capacity = self._prop_levels_capacity[level]
    self.level = level

def double(target):
  return target*2

class Unit():

  def __init__(self, level=1):
    self.hp_init = self._prop_levels_hp[level]
    self.hp_cur = self.hp_init 
    self.dps = self._prop_levels_dps[level]
    self.cost = self._prop_levels_cost[level]

  def printStats(self):
    print "Unit Type: ", self.name
    print "  hp: ", self.hp_cur
    print "  dps: ", self.dps
    print "  cost: ", self.cost
    print ""

  def printHpCur(self):
    print "HpCur: ", self.hp_cur


  def mapHpLevels(self):
    newmap = map(double, self._prop_levels_hp.values() )
    print self._prop_levels_hp
    print newmap

  def printCostLevels(self):
    self.printLevels( self._prop_levels_cost )

  def printLevels(self, prop_levels):
    print "Values: ", prop_levels.values()

  def attack(self, target):
    target.hp_cur -= self.dps

  def isAlive(self):
    return ( self.hp_cur > 0 )

  def setTarget(self, target):
    self._target = target

  def getTarget(self):
    return self._target

  
class Barbarian(Unit):
  name = "Barbarian"
  _prop_levels_hp = { 
      1:45,
      2:54, 
      3:65,
      4:78,
      5:95,
      6:110
  }

  _prop_levels_dps = { 
      1:8,
      2:11, 
      3:14,
      4:18,
      5:23,
      6:26,
  }

  _prop_levels_cost = { 
      1:25,
      2:40, 
      3:60,
      4:80,
      5:100,
      6:150
  }

  _prop_levels_cost_list = [ 
      25,
      40, 
      60,
      80,
      100,
      150
  ]

class Archer(Unit):
  name = "Archer"
  _prop_levels_hp = { 
      2:23, 
      3:28,
  }

  _prop_levels_dps = { 
      2:9, 
      3:12,
  }

  _prop_levels_cost = { 
      2:40, 
      3:80,
  }

class GameInstance:
  _units = []

  _attacking_units = []
  _defending_units = []

  def addAttackingUnit(self, newUnit):
    self._attacking_units.append( newUnit )

  def numAttackingUnits(self):
    return len(self._attacking_units)

  def addDefendingUnit(self, newUnit):
    self._defending_units.append( newUnit )

  def numDefendingUnits(self):
    return len(self._defending_units)

  def acquireTargets(self):
    pass

curGame = GameInstance()
barbarian = Barbarian(2)
curGame.addDefendingUnit(barbarian)
archer = Archer(2)
curGame.addAttackingUnit(archer)

barracks = Barracks(4)

print "Archer: ", archer

archer.printHpCur()
barbarian.setTarget(archer)

print "Has target: ", hasattr( barbarian, '_target' )
print "Target: ", barbarian.getTarget()

while ( archer.isAlive() ):
  barbarian.attack(archer)
  archer.printHpCur()

del barbarian._target
print "Has target: ", hasattr( barbarian, '_target' )
# print "Target: ", barbarian.getTarget()


archer.mapHpLevels()
