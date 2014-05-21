# class ArmyPlanner():
#   """
#   Want to explore some functions that would allow me to easily build armies in this damn game
#   """

import random
from numpy import array,arange

class GameBoard():
  width = 40
  height = 40

  def __init__(self):
    self._boardSpots = arange(1600).reshape(40,40)

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
    self.hp_max = self._prop_levels_hp[level]
    self.hp_cur = self.hp_max 
    self.dps = self._prop_levels_dps[level]
    self.cost = self._prop_levels_cost[level]
    self.pos = (random.random((0,40)),random.random((0,40)))

  def printStats(self):
    print("Unit Type: ", self.name)
    print("  hp: ", self.hp_cur)
    print("  dps: ", self.dps)
    print("  cost: ", self.cost)
    print("")

  def printHpCur(self):
    print("HpCur: ", self.hp_cur)


  def mapHpLevels(self):
    newmap = map(double, self._prop_levels_hp.values() )
    print(self._prop_levels_hp)
    # Python 2 way 
    # print(*newmap)
    # Python 3 way 
    #print(*newmap)

  def printCostLevels(self):
    self.printLevels( self._prop_levels_cost )

  def printLevels(self, prop_levels):
    print("Values: ", prop_levels.values())

  def attack(self):
    self._target.hp_cur -= self.dps
    if ( self._target.isAlive() == False ):
      del self._target

  def kill(self):
    while hasattr( self, '_target' ):
      self._target.printHpCur()
      self.attack()


  def isAlive(self):
    return ( self.hp_cur > 0 )

  def setTarget(self, target):
    self._target = target

  def getTarget(self):
    return self._target

  def hasTarget(self):
    return hasattr( self, '_target' )
  
class Barbarian(Unit):
  name = "Barbarian"
  _range = 1
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
  _range = 5
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

class Battle:
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

  def step(self):
    for curAttacker in self._attacking_units:
      findTarget(curAttacker, self._defending_units)
      print("CurAttacker: ", curAttacker)

def findTarget(attacker, targets):
  attacker.setTarget( random.choice(targets) )
  

curGame = Battle()

barbarian = Barbarian(2)
curGame.addDefendingUnit(barbarian)
archer = Archer(2)
curGame.addDefendingUnit(archer)

archer = Archer(2)
barbarian = Barbarian(2)
curGame.addAttackingUnit(archer)

# findTarget(archer, curGame._defending_units)


curGame.step()

print("TargetNew: ", archer.getTarget() )

# newTuple = (archer, curGame._defending_units)
# print("Tuple: ", newTuple)


barbarian.setTarget(archer)

board = GameBoard()
print(board._boardSpots)
