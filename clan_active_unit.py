from clan_unit import Unit


class ActiveUnit(Unit):
    name = "Abstract ActiveUnit"

    def __init__(self, level=1):
        super(ActiveUnit, self).__init__(level)
        self.dps = self._prop_levels_dps[level]
        self.lastAttack = 0.0
        self.attackSpeed = 1.0
        self.target = None

    def cooldown_percentage(self, gameTime):
        coolDownPercentage = (gameTime - self.lastAttack)/self.attackSpeed
        if (coolDownPercentage > 1.0):
            return 1.0
        else:
            return coolDownPercentage

    def attack_if_possible(self, gameTime):
        if ( self.distance_from(self.target) < self._range ):
            if (self.lastAttack + self.attackSpeed < gameTime):
                self.lastAttack = gameTime
                self.attack()

    def attack(self):
        self.target.hp_cur -= self.dps
        if (self.target.is_alive() is False):
            del self.target
            self.target = None

    def kill(self):
        while hasattr(self, 'target'):
            self.attack()

    def has_target(self):
        return hasattr(self, 'target')

    def acquire_target(self, enemyUnits):
        livingUnits = [unit for unit in enemyUnits if unit.hp_cur > 0]
        distanceList = ([(idx, self.distance_from(enemyUnit))
                         for idx, enemyUnit in enumerate(livingUnits)])

        try:
            targetTuple = min(distanceList, key=lambda x: x[1])
            self.target = livingUnits[targetTuple[0]]
        except ValueError:
            self.target = None

    def drawing_info(self):
        return self.color, (int(self.pos_3d[0]), int(self.pos_3d[1])), self.width, self.fill

    def move_up(self):
        self.pos_3d[1] += 1

    def move(self, moveVec):
        self.pos_3d += moveVec

    def repr_json(self):
        stats = dict(
            dps=self.dps,
        )
        parentStats = super(ActiveUnit, self).repr_json()
        return dict(list(parentStats.items()) + list(stats.items()))
