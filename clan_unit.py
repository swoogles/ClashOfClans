class Unit():
  _table = "unit"
  name = "Abstract Unit"

  def __init__(self, level=1):
    self.level = level
    self.hp_max = self._prop_levels_hp[level]
    self.hp_cur = self.hp_max 
    self.dps = self._prop_levels_dps[level]
    self.cost = self._prop_levels_cost[level]
    # self.pos = (random.random((0,40)),random.random((0,40)))

  def copyFromJSON(self, json):
    self.level = json.get('cost',None)
    self.hp_max = json.get('hp_max',None)
    self.hp_cur = json.get('hp_cur',None)
    self.dps = json.get('dps',None)
    self.cost = json.get('cost',None)

  def printStats(self):
    print "Unit Type: ", self.name
    print "  hp: ", self.hp_cur
    print "  dps: ", self.dps
    print "  cost: ", self.cost
    print ""

  def printHpCur(self):
    print "HpCur: ", self.hp_cur


  def mapHpLevels(self):
    newmap = map(double, self._prop_levels_hp.values() )
    print self._prop_levels_hp

  def printCostLevels(self):
    self.printLevels( self._prop_levels_cost )

  def printLevels(self, prop_levels):
    print "Values: ", prop_levels.values()

  def attack(self):
    self._target.hp_cur -= self.dps
    if ( self._target.isAlive() == False ):
      del self._target

  def kill(self):
    while hasattr( self, '_target' ):
      self._target.printHpCur()
      self.attack()


  def isAlive(self):
    return ( self.hp_cur > 0 )

  def setTarget(self, target):
    self._target = target

  def getTarget(self):
    return self._target

  def hasTarget(self):
    return hasattr( self, '_target' )

  def sql_getTable(self):
    return self._table 

  def reprJSON(self):
    return dict(
        cost=self.cost,
        dps=self.dps, 
        hp_cur=self.hp_cur, 
        hp_max=self.hp_max, 
        level=self.level, 
        name=self.name, 
    )
