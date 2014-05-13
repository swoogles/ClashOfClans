# class ArmyPlanner():
#   """
#   Want to explor some functions that would allow me to easily build armies in this damn game
#   """

class Unit():
  prop_levels_hp = {}
  prop_levels_dps = {}
  prop_levels_cost = {}

  def __init__(self, level=0):
    x = 10

  
class Barbarian(Unit):
  Unit.prop_levels_hp[2]=54
  Unit.prop_levels_hp[3]=65

  Unit.prop_levels_dps[2] = 11
  Unit.prop_levels_dps[3] = 14

  Unit.prop_levels_cost[2] = 40
  Unit.prop_levels_cost[3] = 60

  def __init__(self, level=2):
    Unit.__init__(self)
    self.hp = self.prop_levels_hp[level]
    self.dps = self.prop_levels_dps[level]
    self.cost = self.prop_levels_cost[level]

class Archer(Unit):
  Unit.prop_levels_hp[2]=23
  Unit.prop_levels_hp[3]=28

  Unit.prop_levels_dps[2] = 9
  Unit.prop_levels_dps[3] = 12

  Unit.prop_levels_cost[2] = 80
  Unit.prop_levels_cost[3] = 40

  def __init__(self, level=2):
    Unit.__init__(self)
    self.hp = self.prop_levels_hp[level]
    self.dps = self.prop_levels_dps[level]
    self.cost = self.prop_levels_cost[level]

firstBarb = Barbarian(2)
archer = Archer(2)

print "Barbarian.hp: ", firstBarb.hp
print "Barbarian.dps: ", firstBarb.dps
print "Barbarian.cost: ", firstBarb.cost

print "archer.hp: ", archer.hp
print "archer.dps: ", archer.dps
print "archer.cost: ", archer.cost
