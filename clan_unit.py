from numpy import array, random, linalg
import pygame

BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)


class Unit():
  # Define some colors
  _table = "unit"
  name = "Abstract Unit"
  width = 1
  color = WHITE
  fill = 0


  def __init__(self, level=1):
    self.level = level
    self.hp_max = self._prop_levels_hp[level]
    self.hp_cur = self.hp_max 
    self.cost = self._prop_levels_cost[level]
    self.pos = random.randint(0,40)
    self.pos_3d = array( [random.randint(0,40)*1.0,random.randint(0,40)*1.0,0] )


  def copyFromJSON(self, json):
    for key,value in json.items():
      setattr(self, key, value)

  def mapHpLevels(self):
    newmap = map(double, self._prop_levels_hp.values() )
    print( self._prop_levels_hp)

  def printCostLevels(self):
    self.printLevels( self._prop_levels_cost )

  def printLevels(self, prop_levels):
    print( "Values: ", prop_levels.values())

  def distanceFrom(self, target):
    return linalg.norm(target.pos_3d - self.pos_3d)

  def unitVecTo(self, target):
    return (target.pos_3d - self.pos_3d) / linalg.norm(target.pos_3d - self.pos_3d)

  def isAlive(self):
    return ( self.hp_cur > 0 )

  def sql_getTable(self):
    return self._table 

  # Use some variant of this to determine fields
  # [print ("Var: ", var) for var in vars(attackingList[0])]
  def reprJSON(self):
    return dict(
        [( var, getattr(self,var) ) for var in vars(self) 
          if var != 'target']
    )
