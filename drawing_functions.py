import pygame
import itertools
from clan_active_unit import ActiveUnit
from clan_stationary_unit import Structure, Wall

PI = 3.14
PIXELS_PER_SPACE = 30

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def scale_tuple_for_drawing(origTuple, scalar):
    return tuple([e * scalar for e in origTuple])

def draw_active_unit(screen, unit, gameTime):
    color, pos, width, fill = unit.drawing_info()
    drawWidth = width * PIXELS_PER_SPACE
    scaledPos = scale_tuple_for_drawing(pos, PIXELS_PER_SPACE)
    pygame.draw.circle(
        screen, color, scaledPos, drawWidth, fill)
    myRect = pygame.Rect(scaledPos[0]-drawWidth,scaledPos[1]-drawWidth,drawWidth*2,drawWidth*2)
    arcLength = unit.cooldown_percentage(gameTime) * 2 * PI
    pygame.draw.arc(screen, RED, myRect, 0, arcLength, 4)

    if unit.target is not None:
        targetPos = (unit.target.pos_3d[0], unit.target.pos_3d[1])
        scaledTargetPos = scale_tuple_for_drawing(targetPos, PIXELS_PER_SPACE)
        pygame.draw.line(
            screen, WHITE, scaledPos, scaledTargetPos, 1)

def draw_structure(screen, unit):
    color, spatialInfo, fill = unit.drawing_info()
    scaledSpatialInfo = scale_tuple_for_drawing(spatialInfo, PIXELS_PER_SPACE)
    color = WHITE
    pygame.draw.rect(screen, color, scaledSpatialInfo, fill)

def draw_target_marker(screen, unit, pixelsPerSpace):
    # initialize font; must be called after 'pygame.init()' to avoid 'Font not
    # Initialized' error
    myfont = pygame.font.SysFont("monospace", 25)
    # render text
    targetLabel = myfont.render("X", 1, (255, 255, 0))

    screen.blit(targetLabel, ( (unit.pos_3d[0] - unit.width / 3) * pixelsPerSpace, 
                                (unit.pos_3d[1] - unit.width / 3) * pixelsPerSpace))

def draw_teams(screen, defendingList, attackingList, targetedUnits, gameTime):
    for unit in itertools.chain(defendingList, attackingList):
        if unit.is_alive():
            if isinstance(unit, ActiveUnit):
                draw_active_unit(screen, unit, gameTime)
            elif isinstance(unit, Structure):
                draw_structure(screen, unit)

    for targetedUnit in targetedUnits:
        draw_target_marker(screen, targetedUnit, PIXELS_PER_SPACE )


