from numpy import array, random, linalg

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


class Unit(object):
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
        self.pos = random.randint(0, 40)
        self.pos_3d = array(
            [random.randint(0, 40) * 1.0, random.randint(0, 40) * 1.0, 0])

    def copy_from_json(self, json):
        for key, value in json.items():
            setattr(self, key, value)

    def print_cost_levels(self):
        self.print_levels(self._prop_levels_cost)

    def print_levels(self, prop_levels):
        print("Values: ", prop_levels.values())

    def distance_from(self, target):
        return linalg.norm(target.pos_3d - self.pos_3d)

    def unit_vec_to(self, target):
        return (target.pos_3d - self.pos_3d) / linalg.norm(target.pos_3d - self.pos_3d)

    def is_alive(self):
        return (self.hp_cur > 0)

    def sql_get_table(self):
        return self._table

    def repr_json(self):
        return dict(
            [(var, getattr(self, var)) for var in vars(self)
             if var != 'target']
        )

    _prop_levels_cost = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }

    _prop_levels_dps = {
        1: 1,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }

    _prop_levels_hp = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }

    _prop_levels_cost_list = [
        0,
        0,
        0,
        0,
        0,
        0,
    ]
