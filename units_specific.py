from clan_unit import Unit
class Barbarian(Unit):
  name = "Barbarian"
  _range = 1

  _prop_levels_cost = { 
      1:25,
      2:40, 
      3:60,
      4:80,
      5:100,
      6:150
  }

  _prop_levels_dps = { 
      1:8,
      2:11, 
      3:14,
      4:18,
      5:23,
      6:26,
  }

  _prop_levels_hp = { 
      1:45,
      2:54, 
      3:65,
      4:78,
      5:95,
      6:110
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
  _range = 5
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

