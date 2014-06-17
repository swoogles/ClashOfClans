# class ArmyPlanner():
#   """
#   Want to explore some functions that would allow me to easily build armies in this damn game
#   """

from clan_bomb import Bomb
from units_specific import Barbarian, Archer
from units_specific import Barbarian, Archer
from clan_unit import Unit
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

def insertUnit(session, targetUnit):
  table = targetUnit.sql_getTable()

  json = targetUnit.reprJSON()
  values = json.keys()

  columns = [ val for val in values]
  columns = str(columns).strip('[]').replace("\'","")

  valueSubs = ['%(' + val + ')s' for val in values]

  valueSubsString = str(valueSubs).strip('[]').replace("\'","")

  _query = " INSERT INTO " + table + " ( " + columns + " ) \
  VALUES ( " + valueSubsString + ") ";

  session.execute( _query, json)

def queryAll(session, targetUnit):
  table = targetUnit.sql_getTable()
  _query = "SELECT * FROM " + table

  user_rows = session.execute( _query )
  for row in user_rows:
    print( "Row: ", row)

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

cluster = Cluster()
session = cluster.connect('demo')

copiedBarbarian = Barbarian()
copiedBarbarian.copyFromJSON( barbarian.reprJSON() )

print( "\nTargetNew: ", copiedBarbarian.reprJSON() )
# queryAll(session, barbarian)
insertUnit(session, barbarian)

bomb = Bomb(2)

session.shutdown();
