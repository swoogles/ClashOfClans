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
import itertools
from database_functions import *

# Import a library of functions called 'pygame'
import pygame
# Initialize the game engine
pygame.init()

FPS = 10
PIXELS_PER_SPACE = 30

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)


class GameBoard():
  width = 40
  height = 40

  def __init__(self):
    self._boardSpots = arange(1600).reshape(self.width,self.height)

class Barracks():
  _prop_levels_capacity = {}
  _prop_levels_capacity[4] = 35
  _prop_levels_capacity[5] = 40
  _prop_levels_capacity[6] = 45

  def __init__(self, level=1):
    self.capacity = self._prop_levels_capacity[level]
    self.level = level

def printUnit(session, targetUnit):
  print("unit: ", targetUnit.reprJSON() )

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

cluster = Cluster()
session = cluster.connect('demo')

cqlFile = open('./data.cql', encoding='utf-8')

resetDB(session, cqlFile)

# queryAll(session, barbarian)
# insertUnit(session, barbarian)
unitList = [ Barbarian() for i in range(5)]

# Pythonically insert all the new units
# [insertUnit(session, barbarian)  for barbarian in unitList]
# [print( barbarian.reprJSON().get("pos_3d") )  for barbarian in unitList]

barbarian.color = GREEN

# bomb = Bomb(2)
# unitList.append(bomb)

# Opening and setting the window size
size = (board.width*PIXELS_PER_SPACE, board.height*PIXELS_PER_SPACE)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bill's Cool Game")

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
  screen.fill(BLACK)
  clock.tick(FPS)
  # --- Main event loop
  barbarian.acquireTarget(unitList)
  targetedUnit = barbarian.getTarget()
  if targetedUnit is not None:
    targetedUnit.color = RED
    if barbarian.distanceFrom(targetedUnit) > (barbarian.width+targetedUnit.width):
      moveVec = barbarian.unitVecTo(targetedUnit)
      barbarian.move(moveVec)
    else:
      barbarian.kill()


  for unit in itertools.chain( unitList, [barbarian] ):
    if unit.isAlive():
      if isinstance(unit, ActiveUnit):
        color, pos, width = unit.drawingInfo()
        # print("Pos:", pos)
        # scaledPos = pos
        scaledPos = tuple( [ e * PIXELS_PER_SPACE for e in pos ] )
        # print("scaledPos:", scaledPos)
        pygame.draw.circle(screen, color, scaledPos, width * PIXELS_PER_SPACE, 1)
      elif isinstance(unit, DefensiveUnit):
        color, spatialInfo = unit.drawingInfo()
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
      if event.key == pygame.K_q:
        done = True # Flag that we are done so we exit this loop
        screen.fill(WHITE)
        pygame.display.flip()
        pygame.quit()
      print("User pressed a key.")
    elif event.type == pygame.KEYUP:
      print("User let go of a key.")
    elif event.type == pygame.MOUSEBUTTONDOWN:
      print("User pressed a mouse button")


session.shutdown();
