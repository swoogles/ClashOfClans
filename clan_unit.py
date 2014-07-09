from numpy import array, random, linalg

class Unit():
  _table = "unit"
  name = "Abstract Unit"

  def __init__(self, level=1):
    self.level = level
    self.hp_max = self._prop_levels_hp[level]
    self.hp_cur = self.hp_max 
    self.cost = self._prop_levels_cost[level]
    self.pos = random.randint(0,40)
    self.pos_3d = array( [random.randint(0,40),random.randint(0,40),random.randint(0,40)] )

  def copyFromJSON(self, json):
    self.level = json.get('cost',None)
    self.hp_max = json.get('hp_max',None)
    self.hp_cur = json.get('hp_cur',None)
    self.dps = json.get('dps',None)
    self.cost = json.get('cost',None)
    self.pos = json.get('pos',None)
    self.pos_3d = json.get('pos_3d',None)

  def mapHpLevels(self):
    newmap = map(double, self._prop_levels_hp.values() )
    print( self._prop_levels_hp)

  def printCostLevels(self):
    self.printLevels( self._prop_levels_cost )

  def printLevels(self, prop_levels):
    print( "Values: ", prop_levels.values())

  def distanceFrom(self, target):
    return linalg.norm(self.pos_3d - target.pos_3d)

  def isAlive(self):
    return ( self.hp_cur > 0 )

  def sql_getTable(self):
    return self._table 

  def reprJSON(self):
    return dict(
        cost=self.cost,
        hp_cur=self.hp_cur, 
        hp_max=self.hp_max, 
        level=self.level, 
        name=self.name, 
        pos=self.pos, 
        pos_3d=self.pos_3d, 
    )
