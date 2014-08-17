from numpy import arange, array, empty, vectorize
from graph_tool.all import *

class BoardSpot(object):
    occupied = False
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y

class GameBoard(object):
    width = 8
    height = 8
    ug = Graph(directed=False)

    def __init__(self):
        totalSpots = self.width*self.height
        self._boardSpots = arange(totalSpots).reshape(self.width, self.height)

        # vSite = vectorize(BoardSpot)

        init_arry = arange(totalSpots).reshape((self.width, self.height))

        self.lattice = empty((self.width, self.height), dtype=object)
        # self.lattice[:,:] = vSite()

        self.lattice = array( [ [BoardSpot(i,j) for i in range(self.height)] for j in range(self.width) ],
                                    dtype=object)


        # graphMain = Graph()
        # for i in range(4):
        #     for j in range(4):
        #         self.find_neighbors(i,j)



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
        width, height = self.lattice.shape
        print("width %s", width)
        print("height %s", height)
        for row in range(targetRow-1, targetRow+2):
            for col in range(targetCol-1, targetCol+2):
                finalRow = row
                finalCol = col
                if row < 0:
                    finalRow = height-1

                if row > height-1:
                    finalRow = 0

                if col < 0:
                    finalCol = width-1

                if col > width-1:
                    print("Col:", col)
                    finalCol = 0

                spotList.append( self.lattice[finalRow][finalCol] )
                # if i > 0 and i < len(self.lattice[row]):
                #     if j > 0 and i < len(self.lattice[row]):
                # Out[9]: (4, 4)

        return spotList


