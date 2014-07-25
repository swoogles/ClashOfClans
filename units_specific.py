from clan_active_unit import ActiveUnit
from webcolors import name_to_rgb
import random


class Barbarian(ActiveUnit):
    # name = "Barbarian"
    _range = 1

    def __init__(self, level=1):
        super(Barbarian, self).__init__(level)
        self.name = "Barbarian" + str(random.randint(0, 1000))
        self.color = name_to_rgb('blue')

    _prop_levels_cost = {
        1: 25,
        2: 40,
        3: 60,
        4: 80,
        5: 100,
        6: 150
    }

    _prop_levels_dps = {
        1: 8,
        2: 11,
        3: 14,
        4: 18,
        5: 23,
        6: 26,
    }

    _prop_levels_hp = {
        1: 45,
        2: 54,
        3: 65,
        4: 78,
        5: 95,
        6: 110
    }

    _prop_levels_cost_list = [
        25,
        40,

        60,
        80,
        100,
        150
    ]


class Archer(ActiveUnit):
    name = "Archer"

    def __init__(self, level=1):
        super(Archer, self).__init__(level)
        self.name = "Archer" + str(random.randint(0, 1000))
        self.color = name_to_rgb('yellow')

    _range = 5
    _prop_levels_hp = {
        1: 1,
        2: 23,
        3: 28,
    }

    _prop_levels_dps = {
        1: 1,
        2: 9,
        3: 12,
    }

    _prop_levels_cost = {
        1: 1,
        2: 40,
        3: 80,
    }
