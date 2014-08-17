#   """
#   Want to explore some functions that would allow me to easily build armies in this damn game
#   """

# Run file in interpreter:
# exec(open("./armyplanner.py").read())

# from clan_bomb import Bomb
from units_specific import Barbarian, Archer
from clan_active_unit import ActiveUnit
from clan_stationary_unit import Wall
from game_mechanics import Battle
from drawing_functions import draw_teams
from numpy import array
# from database_functions import *
from webcolors import *
from user_input import process_events
from colors import ClanColors
from gameboard import GameBoard

import configparser 

# Import a library of functions called 'pygame'
import pygame
# Initialize the game engine
pygame.init()


class ClanConfig(object):
    PIXELS_PER_SPACE = 0
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.PIXELS_PER_SPACE = int(config['DEFAULT']['PixelsPerSpace'])

curConfig = ClanConfig()
print( curConfig.PIXELS_PER_SPACE )

FPS = 60

curBattle = Battle()

barbarian = Barbarian(2)
curBattle.add_defending_unit(barbarian)
archer = Archer(2)
curBattle.add_defending_unit(archer)

board = GameBoard()
board.printSpots()
# print(board.find_neighbors(1,1))
neighbors = board.find_neighbors(1,7)

for neighbor in neighbors:
    print("Neighbor.pos:", neighbor.x, neighbor.y)

for i in range(0,2):
    print("i: ", i)

defendingList = [Barbarian() for i in range(5)]
defendingList.extend(Archer() for i in range(5))

wallList = [Wall() for i in range(5)]
for i in range(5):
    wallList[i].pos_3d = array([10, i+10, 0])
defendingList.extend(wallList)

attackingList = [Barbarian() for i in range(4)]
for attacker in attackingList:
    attacker.color = ClanColors.GREEN
    attacker.fill = 1


screenSize = (board.width * curConfig.PIXELS_PER_SPACE, board.height * curConfig.PIXELS_PER_SPACE)
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Bill's Cool Game")



def attack_team(attackingList, defendingList, targetedUnits):
    for attacker in attackingList:
        if isinstance(attacker, ActiveUnit) and attacker.is_alive():
            if attacker.target is None:
                attacker.acquire_target(defendingList)

            targetedUnit = attacker.target

            if targetedUnit is not None:
                targetedUnits.append(targetedUnit)

                attacker.attack_if_possible(gameTime)

# Loop until the user clicks the close button.
done = False
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
gameTime = 0.0
# -------- Main Program Loop -----------
while not done:
    screen.fill(ClanColors.BLACK)
    clock.tick(FPS)
    gameTime += 1.0 / FPS
    # --- Main event loop
    targetedUnits = []
    attack_team(attackingList, defendingList, targetedUnits)
    attack_team(defendingList, attackingList, targetedUnits)

    draw_teams(screen, defendingList, attackingList, targetedUnits, gameTime)

    pygame.display.update()
    pygame.display.flip()

    done = process_events(screen, curConfig.PIXELS_PER_SPACE, attackingList, defendingList)
