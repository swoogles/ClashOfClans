# class ArmyPlanner():
#   """
#   Want to explore some functions that would allow me to easily build armies in this damn game
#   """

class Barracks():
  _prop_levels_capacity = {}
  # _prop_levels_capacity[1] =
  # _prop_levels_capacity[2] =
  # _prop_levels_capacity[3] =
  _prop_levels_capacity[4] = 35
  _prop_levels_capacity[5] = 40
  _prop_levels_capacity[6] = 45

  def __init__(self, level=1):
    self.capacity = self._prop_levels_capacity[level]
    self.level = level

class Unit():

  def __init__(self, level=1):
    self.hp = self._prop_levels_hp[level]
    self.dps = self._prop_levels_dps[level]
    self.cost = self._prop_levels_cost[level]

  def printStats(self):
    print "Unit Type: ", self.name
    print "  hp: ", self.hp
    print "  dps: ", self.dps
    print "  cost: ", self.cost
    print ""

  def printHpLevels(self):
    print self._prop_levels_hp

  def printCostLevels(self):
    self.printLevels( self._prop_levels_cost )

  def printLevels(self, prop_levels):
    print "Values: ", prop_levels.values()

  
class Barbarian(Unit):
  name = "Barbarian"
  _prop_levels_hp = { 
      1:45,
      2:54, 
      3:65,
      4:78,
      5:95,
      6:110
  }

  _prop_levels_dps = { 
      1:8,
      2:11, 
      3:14,
      4:18,
      5:23,
      6:26,
  }

  _prop_levels_cost = { 
      1:25,
      2:40, 
      3:60,
      4:80,
      5:100,
      6:150
  }

  _prop_levels_cost_list = [ 
      25,
      40, 
      60,
      80,
      100,
      150
  ]

class Archer(Unit):
  name = "Archer"
  _prop_levels_hp = { 
      2:23, 
      3:28,
  }

  _prop_levels_dps = { 
      2:9, 
      3:12,
  }

  _prop_levels_cost = { 
      2:40, 
      3:80,
  }

barbarian = Barbarian(2)
archer = Archer(2)

barracks = Barracks(4)

barbarian.printStats()

print "barracks.level: ", barracks.level
print "barracks.capacity: ", barracks.capacity

archer.printStats()
archer.printHpLevels()

barbarian.printCostLevels()
archer.printCostLevels()
