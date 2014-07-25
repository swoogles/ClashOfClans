class Battle(object):
    _units = []

    _attacking_units_queued = []
    _attacking_units_deployed = []
    _defending_units = []

    def add_attacking_unit(self, newUnit):
        self._attacking_units_queued.append(newUnit)

    def num_attacking_units(self):
        return len(self._attacking_units_queued) + len(self._attacking_units_deployed)

    def add_defending_unit(self, newUnit):
        self._defending_units.append(newUnit)

    def num_defending_units(self):
        return len(self._defending_units)

    def deploy_attacking_unit(self, targetUnitIdx):
        self._attacking_units_deployed.append(
            self._attacking_units_queued.pop(targetUnitIdx))
