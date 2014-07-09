# class ArmyPlanner():
#   """
#   Want to explore some functions that would allow me to easily build armies in this damn game
#   """

# Run file in interpreter:
# exec(open("./armyplanner.py").read())

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

def resetDB(session, schemaDataFile):
  # session.execute( cqlCommands)
  line_number = 0
  with open('./data.cql', encoding='utf-8') as schemaDataFile:
    for command in schemaDataFile:
      # print('{:>4} {}'.format(line_number, command.rstrip()))  
      session.execute(command.strip())
      # line_number += 1


def printUnit(session, targetUnit):
  print("unit: ", targetUnit.reprJSON() )

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

cqlFile = open('./data.cql', encoding='utf-8')

resetDB(session, cqlFile)

copiedBarbarian = Barbarian()
copiedBarbarian.copyFromJSON( barbarian.reprJSON() )

# queryAll(session, barbarian)
# insertUnit(session, barbarian)
unitList = [ Barbarian() for i in range(5)]

# Pythonically insert all the new units
# [insertUnit(session, barbarian)  for barbarian in unitList]
# [print( barbarian.reprJSON().get("pos_3d") )  for barbarian in unitList]

print( "Main Pos: ", copiedBarbarian.reprJSON().get("pos_3d") )

for barbarian in unitList:
  print( "Pos: ", barbarian.reprJSON().get("pos_3d") )
  print( "Distance: ", copiedBarbarian.distanceFrom(barbarian) ) 

distanceList = ([ (idx, copiedBarbarian.distanceFrom(barbarian) ) for idx, barbarian in enumerate(unitList) ])


print ("distanceList: ", distanceList)

print("Max:", max(distanceList, key=lambda x: x[1]) )
# bomb = Bomb(2)

session.shutdown();
