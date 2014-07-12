# class ArmyPlanner():
#   """
#   Want to explore some functions that would allow me to easily build armies in this damn game
#   """

# Run file in interpreter:
# exec(open("./armyplanner.py").read())

from clan_bomb import Bomb
from units_specific import Barbarian, Archer
from clan_unit import Unit
from clan_active_unit import ActiveUnit
from clan_stationary_unit import DefensiveUnit
from game_mechanics import Battle
from numpy import array,arange
from cassandra.cluster import Cluster
import json

# Import a library of functions called 'pygame'
import pygame
# Initialize the game engine
pygame.init()

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)


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

copiedBarbarian.color = GREEN
copiedBarbarian.acquireTarget(unitList)

targetedUnit = copiedBarbarian.getTarget()
targetedUnit.color = RED

print("TargetedUnit.alive: ", targetedUnit.isAlive() )

copiedBarbarian.kill()

print("TargetedUnit.alive: ", targetedUnit.isAlive() )
bomb = Bomb(2)
unitList.append(bomb)

# Opening and setting the window size
size = (40*10, 40*10)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bill's Cool Game")

drawingList = unitList.append(copiedBarbarian)

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
  # --- Main event loop
  # pygame.display.flip()
  for barbarian in unitList:
    pos3d = barbarian.reprJSON().get("pos_3d")
    xPos = pos3d[0]*10
    yPos = pos3d[1]*10
    width = 10
    spatialInfo = [ xPos, yPos, width, width ]
    drawingInfo = (WHITE, spatialInfo)
    if isinstance(barbarian, ActiveUnit):
      color, pos, width = barbarian.drawingInfo()
      pygame.draw.circle(screen, color, pos, width, 1)
    elif isinstance(barbarian, DefensiveUnit):
      color, spatialInfo = barbarian.drawingInfo()
      pygame.draw.rect(screen, color, spatialInfo, 1)

  pygame.display.update()
  pygame.display.flip()

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print("User asked to quit.")
      done = True # Flag that we are done so we exit this loop
      # --- Game logic should go here
      # --- Drawing code should go here
      # First, clear the screen to white. Don't put other drawing commands
      # above this, or they will be erased with this command.
      screen.fill(WHITE)
      # --- Go ahead and update the screen with what we've drawn.
      pygame.display.flip()
      # --- Limit to 60 frames per second
      clock.tick(60)
      pygame.quit()
    elif event.type == pygame.KEYDOWN:
      # pygame.draw.rect(screen, WHITE, [55, 500, 10, 5], 1)
      # pygame.draw.rect(screen, WHITE, [55, 200, 10, 5], 1)
      # pygame.display.update()
      # pygame.display.flip()
      # clock.tick(60)
      print("User pressed a key.")
    elif event.type == pygame.KEYUP:
      print("User let go of a key.")
    elif event.type == pygame.MOUSEBUTTONDOWN:
      print("User pressed a mouse button")


session.shutdown();
