#   """
#   Want to explore some functions that would allow me to easily build armies in this damn game
#   """

# Run file in interpreter:
# exec(open("./armyplanner.py").read())

# from clan_bomb import Bomb
from units_specific import Barbarian, Archer
from clan_active_unit import ActiveUnit
from clan_stationary_unit import DefensiveUnit
from game_mechanics import Battle
from numpy import array, arange
from cassandra.cluster import Cluster
import json
import itertools
from database_functions import *
from webcolors import *
# from colors import ClanColors

# Import a library of functions called 'pygame'
import pygame
# Initialize the game engine
pygame.init()

FPS = 60
PIXELS_PER_SPACE = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class GameBoard(Object):
    width = 40
    height = 40

    def __init__(self):
        self._boardSpots = arange(1600).reshape(self.width, self.height)


class Barracks(Object):
    _prop_levels_capacity = {}
    _prop_levels_capacity[4] = 35
    _prop_levels_capacity[5] = 40
    _prop_levels_capacity[6] = 45

    def __init__(self, level=1):
        self.capacity = self._prop_levels_capacity[level]
        self.level = level

curBattle = Battle()

barbarian = Barbarian(2)
curBattle.addDefendingUnit(barbarian)
archer = Archer(2)
curBattle.addDefendingUnit(archer)

nextBarbarian = Barbarian(2)
print("Orig:", nextBarbarian.reprJSON())
nextBarbarian.copyFromJSON(barbarian.reprJSON())
curBattle.addAttackingUnit(archer)
nextBarbarian.reprJSON()
print("Copied:", nextBarbarian.reprJSON())

# curBattle.step()
# barbarian.setTarget(archer)

board = GameBoard()

# Cassandra DB commands
# cluster = Cluster()
# session = cluster.connect('demo')
# cqlFile = open('./data.cql', encoding='utf-8')
# resetDB(session, cqlFile)

defendingList = [Barbarian() for i in range(5)]
defendingList.extend(Archer() for i in range(5))

# [False for x.fill in defendingList]

# Pythonically insert all the new units
# [insertUnit(session, barbarian)  for barbarian in defendingList]
# [print( barbarian.reprJSON().get("pos_3d") )  for barbarian in defendingList]


attackingList = [Barbarian() for i in range(4)]
for attacker in attackingList:
    attacker.color = GREEN
    attacker.fill = 1
# map( lambda x : setattr(x, 'fill', 1), attackingList )
# map( lambda x : setattr(x, 'color', GREEN), attackingList )

# bomb = Bomb(2)
# defendingList.append(bomb)

size = (board.width * PIXELS_PER_SPACE, board.height * PIXELS_PER_SPACE)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bill's Cool Game")

# initialize font; must be called after 'pygame.init()' to avoid 'Font not
# Initialized' error
myfont = pygame.font.SysFont("monospace", 25)

# render text
targetLabel = myfont.render("X", 1, (255, 255, 0))


def attackTeam(attackingList, defendingList, targetedUnits):
    for attacker in attackingList:
        if attacker.isAlive():
            if attacker.target is None:
                attacker.acquireTarget(defendingList)

            targetedUnit = attacker.target

            if targetedUnit is not None:
                targetedUnits.append(targetedUnit)

                if attacker.distanceFrom(targetedUnit) > (attacker.width + targetedUnit.width):
                    moveVec = attacker.unitVecTo(targetedUnit)
                    attacker.move(moveVec)
                else:
                    attacker.attackIfPossible(gameTime)

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
gameTime = 0.0
# -------- Main Program Loop -----------
while not done:
    screen.fill(BLACK)
    clock.tick(FPS)
    gameTime += 1.0 / FPS
    # print("Gametime: ", gameTime )
    # --- Main event loop
    targetedUnits = []
    attackTeam(attackingList, defendingList, targetedUnits)
    attackTeam(defendingList, attackingList, targetedUnits)

    for unit in itertools.chain(defendingList, attackingList):
        if unit.isAlive():
            if isinstance(unit, ActiveUnit):
                color, pos, width, fill = unit.drawingInfo()
                scaledPos = tuple([e * PIXELS_PER_SPACE for e in pos])
                pygame.draw.circle(
                    screen, color, scaledPos, width * PIXELS_PER_SPACE, fill)
                if (unit.target is not None):
                    targetPos = (unit.target.pos_3d[0], unit.target.pos_3d[1])
                    scaledTargetPos = tuple(
                        [e * PIXELS_PER_SPACE for e in targetPos])
                    pygame.draw.line(
                        screen, WHITE, scaledPos, scaledTargetPos, 1)
            elif isinstance(unit, DefensiveUnit):
                color, spatialInfo, fill = unit.drawingInfo()
                pygame.draw.rect(screen, color, spatialInfo, fill)

    for targetedUnit in targetedUnits:
        screen.blit(targetLabel, (targetedUnit.pos_3d[0] * PIXELS_PER_SPACE - targetedUnit.width / 3 *
                                  PIXELS_PER_SPACE, targetedUnit.pos_3d[1] * PIXELS_PER_SPACE - targetedUnit.width / 3 * PIXELS_PER_SPACE))

    pygame.display.update()
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("User asked to quit.")
            done = True  # Flag that we are done so we exit this loop
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
                done = True  # Flag that we are done so we exit this loop
                screen.fill(WHITE)
                pygame.display.flip()
                pygame.quit()
            print("User pressed a key.")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            newUnit = Barbarian()
            newUnit.pos_3d[0] = pos[0] / PIXELS_PER_SPACE
            newUnit.pos_3d[1] = pos[1] / PIXELS_PER_SPACE
            if event.button == 1:
                newUnit.fill = 1
                attackingList.append(newUnit)
            elif event.button == 3:
                defendingList.append(newUnit)


# session.shutdown();
