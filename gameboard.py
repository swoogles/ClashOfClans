from numpy import arange, array, empty, vectorize
from graph_tool.all import *

class BoardSpot(object):
    occupied = False

class GameBoard(object):
    width = 40
    height = 40
    ug = Graph(directed=False)

    def __init__(self):
        self._boardSpots = arange(1600).reshape(self.width, self.height)

        vSite = vectorize(BoardSpot)

        init_arry = arange(1600).reshape((self.width, self.height))

        self.lattice = empty((self.width, self.height), dtype=object)
        self.lattice[:,:] = vSite()

        self.lattice = array( [ [BoardSpot() for i in range(4)] for j in range(4) ],
                                    dtype=object)

        # self.lattice = array( [ [BoardSpot() for i in range(self.width)] for j in range(self.height) ],
        #                             dtype=object)

    def printSpots(self):
        for row in self.lattice:
            for column in row:
                # column.vertex = self.ug.add_vertex()
                print(column,end=",")
            print()

    def find_neighbors(self, targetRow, targetCol):
        spotList = []
        for row in range(targetRow-1, targetRow+2):
            for col in range(targetCol-1, targetCol+2):
                spotList.append( self.lattice[row][col] )

        return spotList


