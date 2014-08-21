from numpy import arange, array, empty, vectorize
from graph_tool.all import *
from queue import Queue

class BoardSpot(object):
    occupied = False
    vertex = None

    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y

class GameBoard(object):
    width = 20
    height = 20


    graphMain = Graph(directed=False)
    color = graphMain.new_vertex_property("int")
    pos = graphMain.new_vertex_property("vector<double>")

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


    def printSpots(self):
        for row in self.lattice:
            for column in row:
                print(column,end=",")
            print()

    def reset_colors(self):
        width, height = self.lattice.shape
        for row in range(0,height):
            for col in range(0,width):
                self.color[self.lattice[row][col].vertex] = 10000
                self.pos[self.lattice[row][col].vertex] = (self.lattice[row][col].x, self.lattice[row][col].y)

    def find_neighbors(self, targetRow, targetCol):
        spotList = []
        width, height = self.lattice.shape
                # myGameBoard.color[myGameBoard.lattice[1][1].vertex] = 10000
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

                if row == targetRow and col == targetCol:
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

myQueue = Queue()
visited = []
frontier = Queue()

startIdx = 5
frontier.put( myGameBoard.lattice[startIdx][startIdx] )


for i in range(startIdx,startIdx+5):
    myGameBoard.reset_colors()
    nextFrontier = Queue()

    while ( frontier.empty() != True ):
        target = frontier.get()
        myGameBoard.color[target.vertex] = 5000
        row = target.y
        col = target.x

        for neighbor in myGameBoard.find_neighbors(row,col):
            if neighbor not in visited:
                nextFrontier.put(neighbor)
                visited.append(neighbor)

        visited.append(target)

    frontier = nextFrontier

    # result = graph_draw(myGameBoard.graphMain, vertex_text=myGameBoard.graphMain.vertex_index, vertex_font_size=4, output_size=(600, 600), vertex_size=4, vertex_color=myGameBoard.color, vertex_fill_color=myGameBoard.color, pos=myGameBoard.pos)
    result = graph_draw(myGameBoard.graphMain, vertex_text=myGameBoard.graphMain.vertex_index, vertex_font_size=4, output_size=(600, 600), vertex_size=4, vertex_color=myGameBoard.color, vertex_fill_color=myGameBoard.color, pos=myGameBoard.pos, output="board"+str(i)+".png")
    print(result)
