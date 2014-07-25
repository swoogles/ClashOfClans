from clan_stationary_unit import DefensiveUnit


class Bomb(DefensiveUnit):
    name = "Bomb"
    _range = 1

    def __init__(self, level=1):
        super().__init__(level)

    _prop_levels_hp = {
        2: 23,
        3: 28,
    }

    _prop_levels_dps = {
        2: 9,
        3: 12,
    }

    _prop_levels_cost = {
        2: 40,
        3: 80,
    }

    # def detectUnits(self, attackingUnits):
    #   if ( filter( lambda x: x
