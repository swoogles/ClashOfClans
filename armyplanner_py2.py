# class ArmyPlanner():
#   """
#   Want to explore some functions that would allow me to easily build armies in this damn game
#   """

import random
from units_specific import Barbarian, Archer
from numpy import array,arange
from cassandra.cluster import Cluster

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


# newTuple = (archer, curGame._defending_units)
# print "Tuple: ", newTuple


barbarian.setTarget(archer)

board = GameBoard()
# print board._boardSpots

last_names = [ 'Rob', 'John' ]

cluster = Cluster()
session = cluster.connect('demo')

jsonNames = {'last_name':'Rob' }

query = "SELECT * FROM users WHERE lastname=%(last_name)s"
query = "SELECT * FROM unit"
# future = session.execute_async(query, [last_names])

futures = []

# for last_name in last_names:
#   futures.append(session.execute_async( query, [last_name] ))

# for last_name in last_names:
# futures.append(session.execute_async( query, jsonNames ))
futures.append(session.execute_async( query, jsonNames ))

for future in futures:
  user_rows = future.result()
  for row in user_rows:
    print "Row: ", row.name, row.cost

print "TargetNew: ", archer.getTarget() 
