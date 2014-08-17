from numpy import arange, array, empty, vectorize
from graph_tool.all import *

class BoardSpot(object):
    occupied = False
    vertex = None
    # def __init__(self, x=0,y=0,vertex):
    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y
        # self.vertex
        # v1 = graphMain.add_vertex()

class GameBoard(object):
    width = 4
    height = 4


    graphMain = Graph(directed=False)
    color = graphMain.new_vertex_property("int")

    def __init__(self):
        totalSpots = self.width*self.height
        self._boardSpots = arange(totalSpots).reshape(self.width, self.height)
        # vSite = vectorize(BoardSpot)

        init_arry = arange(totalSpots).reshape((self.width, self.height))

        self.lattice = empty((self.width, self.height), dtype=object)
        # self.lattice[:,:] = vSite()

        self.lattice = array( [ [BoardSpot(i,j) for i in range(self.height)] for j in range(self.width) ],
                                    dtype=object)
        self.connectSpots()
        self.color[self.lattice[1][1].vertex] = 10000
        # color[1,1] = 0
        # print(self.lattice[1][1].find_neighbors())
        for neighbor in self.find_neighbors(1,1):
            print("Damn")
            self.color[neighbor.vertex] = 5000

    def connectSpots(self):
        width, height = self.lattice.shape
        for row in range(0,height):
            for col in range(0,width):
                self.lattice[row][col].vertex = self.graphMain.add_vertex()

        for row in range(0,height):
            for col in range(0,width):
                neighbors = self.find_neighbors(row,col)
                for neighbor in neighbors:
                    if neighbor.vertex is not None:
                        self.graphMain.add_edge(self.lattice[row][col].vertex, neighbor.vertex)

        # graphMain = Graph()
        # for i in range(4):
        #     for j in range(4):
        #         self.find_neighbors(i,j)



        # self.lattice = array( [ [BoardSpot() for i in range(self.width)] for j in range(self.height) ],
        #                             dtype=object)

    def printSpots(self):
        for row in self.lattice:
            for column in row:
                # column.vertex = self.graphMain.add_vertex()
                print(column,end=",")
            print()

    def find_neighbors(self, targetRow, targetCol):
        spotList = []
        width, height = self.lattice.shape
        # print("Target: ", targetRow, ",", targetCol)
        for row in range(targetRow-1, targetRow+2):
            for col in range(targetCol-1, targetCol+2):
                valid = True
                finalRow = row
                finalCol = col
                if row < 0:
                    finalRow = height-1
                    valid = False

                if row > height-1:
                    finalRow = 0
                    valid = False

                if col < 0:
                    finalCol = width-1
                    valid = False

                if col > width-1:
                    finalCol = 0
                    valid = False

                if valid:
                    spotList.append( self.lattice[finalRow][finalCol] )
                # if i > 0 and i < len(self.lattice[row]):
                #     if j > 0 and i < len(self.lattice[row]):
                # Out[9]: (4, 4)

        return spotList


myGameBoard = GameBoard()

# graph_draw(myGameBoard.graphMain, vertex_text=myGameBoard.graphMain.vertex_index, vertex_font_size=18, output_size=(200, 200))

# age = myGameBoard.graphMain.vertex_properties["age"]

graph_draw(myGameBoard.graphMain, vertex_text=myGameBoard.graphMain.vertex_index, vertex_font_size=30, output_size=(600, 600), output="board.png", vertex_size=4, vertex_color=myGameBoard.color, vertex_fill_color=myGameBoard.color)

