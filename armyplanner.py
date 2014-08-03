#   """
#   Want to explore some functions that would allow me to easily build armies in this damn game
#   """

# Run file in interpreter:
# exec(open("./armyplanner.py").read())

# from clan_bomb import Bomb
from units_specific import Barbarian, Archer
from clan_active_unit import ActiveUnit
from clan_stationary_unit import Structure, Wall
from game_mechanics import Battle
from numpy import arange
import itertools
# from database_functions import *
from webcolors import *
from user_input import process_events
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


class GameBoard(object):
    width = 40
    height = 40

    def __init__(self):
        self._boardSpots = arange(1600).reshape(self.width, self.height)


class Barracks(object):
    _prop_levels_capacity = {}
    _prop_levels_capacity[4] = 35
    _prop_levels_capacity[5] = 40
    _prop_levels_capacity[6] = 45

    def __init__(self, level=1):
        self.capacity = self._prop_levels_capacity[level]
        self.level = level

curBattle = Battle()

barbarian = Barbarian(2)
curBattle.add_defending_unit(barbarian)
archer = Archer(2)
curBattle.add_defending_unit(archer)

board = GameBoard()

defendingList = [Barbarian() for i in range(5)]
defendingList.extend(Archer() for i in range(5))
defendingList.append(Wall())

# Pythonically insert all the new units
# [insertUnit(session, barbarian)  for barbarian in defendingList]


attackingList = [Barbarian() for i in range(4)]
for attacker in attackingList:
    attacker.color = GREEN
    attacker.fill = 1
# map( lambda x : setattr(x, 'color', GREEN), attackingList )

def draw_teams(defendingList, attackingList):
    for unit in itertools.chain(defendingList, attackingList):
        if unit.is_alive():
            if isinstance(unit, ActiveUnit):
                color, pos, width, fill = unit.drawing_info()
                drawWidth = width * PIXELS_PER_SPACE
                scaledPos = tuple([e * PIXELS_PER_SPACE for e in pos])
                pygame.draw.circle(
                    screen, color, scaledPos, drawWidth, fill)
                myRect = pygame.Rect(scaledPos[0]-drawWidth,scaledPos[1]-drawWidth,drawWidth*2,drawWidth*2)
                arcLength = unit.cooldown_percentage(gameTime) * 2 * PI
                pygame.draw.arc(screen, RED, myRect, 0, arcLength,4) # radiant instead of grad

                if (unit.target is not None):
                    targetPos = (unit.target.pos_3d[0], unit.target.pos_3d[1])
                    scaledTargetPos = tuple(
                        [e * PIXELS_PER_SPACE for e in targetPos])
                    pygame.draw.line(
                        screen, WHITE, scaledPos, scaledTargetPos, 1)
        elif isinstance(unit, Wall):
            color, spatialInfo, fill = unit.drawing_info()
            color = WHITE
            pygame.draw.rect(screen, color, spatialInfo, fill)

    for targetedUnit in targetedUnits:
        screen.blit(targetLabel, (targetedUnit.pos_3d[0] * PIXELS_PER_SPACE - targetedUnit.width / 3 *
                                  PIXELS_PER_SPACE, targetedUnit.pos_3d[1] * PIXELS_PER_SPACE - targetedUnit.width / 3 * PIXELS_PER_SPACE))


size = (board.width * PIXELS_PER_SPACE, board.height * PIXELS_PER_SPACE)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Bill's Cool Game")

# initialize font; must be called after 'pygame.init()' to avoid 'Font not
# Initialized' error
myfont = pygame.font.SysFont("monospace", 25)

# render text
targetLabel = myfont.render("X", 1, (255, 255, 0))


def attack_team(attackingList, defendingList, targetedUnits):
    for attacker in attackingList:
        if isinstance(attacker, ActiveUnit) and attacker.is_alive():
            if attacker.target is None:
                attacker.acquire_target(defendingList)

            targetedUnit = attacker.target

            if targetedUnit is not None:
                targetedUnits.append(targetedUnit)

                if attacker.distance_from(targetedUnit) > attacker._range:
                    moveVec = attacker.unit_vec_to(targetedUnit)
                    attacker.move(moveVec)
                else:
                    attacker.attack_if_possible(gameTime)

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
gameTime = 0.0
PI = 3.14
# -------- Main Program Loop -----------
while not done:
    screen.fill(BLACK)
    clock.tick(FPS)
    gameTime += 1.0 / FPS
    # print("Gametime: ", gameTime )
    # --- Main event loop
    targetedUnits = []
    attack_team(attackingList, defendingList, targetedUnits)
    attack_team(defendingList, attackingList, targetedUnits)

    draw_teams(defendingList, attackingList)

    pygame.display.update()
    pygame.display.flip()

    done = process_events(screen, PIXELS_PER_SPACE, attackingList, defendingList)
