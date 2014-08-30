from numpy import arange, array, empty, ndenumerate, vectorize
from graph_tool.all import *
from queue import Queue

numrounds = 4

class BoardSpot(object):
    occupied = False
    vertex = None

    def __init__(self, x=0,y=0):
        self.x = x
        self.y = y

class GameBoard(object):
    width = 25
    height = 25


    graphMain = Graph(directed=False)
    color = graphMain.new_vertex_property("string")
    pos = graphMain.new_vertex_property("vector<double>")

    def __init__(self):
        totalSpots = self.width*self.height
        self._boardSpots = arange(totalSpots).reshape(self.width, self.height)

        init_arry = arange(totalSpots).reshape((self.width, self.height))

        self.lattice = empty((self.width, self.height), dtype=object)

        self.lattice = array( [ [BoardSpot(i,j) for i in range(self.height)] for j in range(self.width) ],
                                    dtype=object)
        self.connectSpots()

    def connectSpots(self):
        width, height = self.lattice.shape
        for (row, col), val in ndenumerate(self.lattice):
            self.lattice[row][col].vertex = self.graphMain.add_vertex()

        for (row, col), val in ndenumerate(self.lattice):
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
        for (row, col), val in ndenumerate(self.lattice):
            self.color[self.lattice[row][col].vertex] = "green"
            self.pos[self.lattice[row][col].vertex] = (self.lattice[row][col].x, self.lattice[row][col].y)

        # Draw walls
        startingDiagonal=12
        squareSize=6
        wallPositions = (
                (3,18),(15,2),(12,1),
                )
        for x,y in wallPositions:
            for row in range(y,y+squareSize):
                for col in range(x,x+squareSize):
                    self.lattice[row][col].occupied = True
                    self.color[self.lattice[row][col].vertex] = "red"

    def find_neighbors(self, targetRow, targetCol):
        spotList = []
        width, height = self.lattice.shape
        
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

                if valid and self.lattice[row][col].occupied is True:
                    valid = False

                if valid:
                    spotList.append( self.lattice[finalRow][finalCol] )

        return spotList

def graphSnapshot(myGameBoard,picCnt,fileName):
    result = graph_draw(
            myGameBoard.graphMain, 
            # vertex_text=myGameBoard.graphMain.vertex_index, 
            vertex_font_size=4, 
            output_size=(600, 600), 
            vertex_size=6, 
            vertex_color=myGameBoard.color, 
            vertex_fill_color=myGameBoard.color, 
            pos=myGameBoard.pos, 
            #Remove output parameter for interactive window
            output=fileName+format(picCnt, '02d')+".png"
            )
    print(result)
    return picCnt + 1


myGameBoard = GameBoard()
myQueue = Queue()
came_from = {}
frontier = Queue()

startIdx = 5
start = myGameBoard.lattice[startIdx][startIdx]
goal = myGameBoard.lattice[startIdx+3][startIdx+2]
frontier.put( start )

picCnt=0

myGameBoard.reset_colors()
fileNameMain="board"
fileNameFrontier="frontier"

for i in range(startIdx,startIdx+numrounds):
    myGameBoard.reset_colors()
    nextFrontier = Queue()

    while ( frontier.empty() != True ):
        target = frontier.get()
        row = target.y
        col = target.x

        for neighbor in myGameBoard.find_neighbors(row,col):
            if neighbor not in came_from:
                came_from[neighbor] = target
                nextFrontier.put(neighbor)

            # came_from.append(target)

    for spot in came_from:
        myGameBoard.color[spot.vertex] = "grey"

    while nextFrontier.empty() == False:
        transitionSpot = nextFrontier.get()
        # if transitionSpot not in came_from:
        myGameBoard.color[transitionSpot.vertex] = "blue"
        frontier.put(transitionSpot)

    picCnt = graphSnapshot(myGameBoard,picCnt,fileNameFrontier)


current = goal
path = [current]
while current != start:
    current = came_from[current]
    path.append(current)

for spot in path:
    myGameBoard.color[spot.vertex] = "orange"

picCnt = graphSnapshot(myGameBoard,picCnt,fileNameFrontier)
