from numpy import arange

class GameBoard(object):
    width = 40
    height = 40

    def __init__(self):
        self._boardSpots = arange(1600).reshape(self.width, self.height)


