# class ArmyPlanner():
#   """
#   Want to explore some functions that would allow me to easily build armies in this damn game
#   """

from units_specific import Barbarian, Archer
from game_mechanics import Battle
from numpy import array,arange
from cassandra.cluster import Cluster
import json

class GameBoard():
  width = 40
  height = 40

  def __init__(self):
    self._boardSpots = arange(1600).reshape(40,40)

class Barracks():
  _prop_levels_capacity = {}
  _prop_levels_capacity[4] = 35
  _prop_levels_capacity[5] = 40
  _prop_levels_capacity[6] = 45

  def __init__(self, level=1):
    self.capacity = self._prop_levels_capacity[level]
    self.level = level

def double(target):
  return target*2

# class DBAccess:
#   _units = []

def insertUnit(targetUnit):
  table = targetUnit.sql_getTable
  _query = " INSERT INTO unit (name, level , cost , dps , hp_max  ) \
  VALUES (%(name)s, %(level)s , %(cost)s , %(dps)s , %(hp_max)s  ) ";
  print "Query: ", _query

def queryAll(targetUnit):
  _query = "SELECT * FROM %(table_name)s"
  table = targetUnit.sql_getTable
  tableName = {'table_name':table}
  futures = []
  futures.append(session.execute_async( query, jsonNames ))

  for future in futures:
    user_rows = future.result()
    for row in user_rows:
      print "Row: ", row.name, row.cost


curBattle = Battle()

barbarian = Barbarian(2)
curBattle.addDefendingUnit(barbarian)
archer = Archer(2)
curBattle.addDefendingUnit(archer)

archer = Archer(2)
barbarian = Barbarian(2)
curBattle.addAttackingUnit(archer)

curBattle.step()
barbarian.setTarget(archer)

board = GameBoard()
# print board._boardSpots

last_names = [ 'Rob', 'John' ]

cluster = Cluster()
# session = cluster.connect('demo')

jsonNames = {'last_name':'Rob' }

query = "SELECT * FROM users WHERE lastname=%(last_name)s"
query = "SELECT * FROM unit"

futures = []

# futures.append(session.execute_async( query, jsonNames ))

# queryAll(Barbarian)
# insertUnit(Barbarian)

print "TargetNew: ", archer.reprJSON() 

# session.shutdown();
