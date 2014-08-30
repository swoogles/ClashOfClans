from numpy import arange, array, empty, ndenumerate, vectorize
from graph_tool.all import *
from queue import Queue

numrounds = 20

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
            target = self.lattice[row][col]
            self.color[target.vertex] = "green"
            self.pos[target.vertex] = (target.x, target.y)

        # Draw walls
        startingDiagonal=12
        squareSize=6
        wallPositions = (
                (3,18),(15,2),(12,1),
                )

        for x,y in wallPositions:
            for row in range(y,y+squareSize):
                for col in range(x,x+squareSize):
                    target = self.lattice[row][col]
                    target.occupied = True
                    self.color[target.vertex] = "red"

    def find_neighbors(self, targetRow, targetCol):
        spotList = []
        width, height = self.lattice.shape

        for row in range(targetRow-1, targetRow+2):
            for col in range(targetCol-1, targetCol+2):
                valid = True
                if not 0 <= row <= height-1:
                    valid = False

                if not 0 <= col <= width-1:
                    valid = False

                # Disallow being neighbor of self
                if row == targetRow and col == targetCol:
                    valid = False

                if valid and not self.lattice[row][col].occupied:
                    spotList.append( self.lattice[row][col] )

        return spotList

def findPath(start, goal, came_from, gameBoard):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)

    return path

def color_path(path,color, gameBoard):
    for spot in path:
        gameBoard.color[spot.vertex] = color

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
goal = myGameBoard.lattice[startIdx][startIdx+17]
frontier.put( start )

picCnt=0

myGameBoard.reset_colors()
fileNameMain="board"
fileNameFrontier="frontier"

curRound = 0
while curRound < numrounds and goal not in came_from:
    myGameBoard.reset_colors()
    nextFrontier = Queue()

    while not frontier.empty():
        target = frontier.get()
        row = target.y
        col = target.x

        for neighbor in myGameBoard.find_neighbors(row,col):
            if neighbor not in came_from:
                came_from[neighbor] = target
                nextFrontier.put(neighbor)

    for spot in came_from:
        myGameBoard.color[spot.vertex] = "grey"

    while not nextFrontier.empty():
        transitionSpot = nextFrontier.get()
        myGameBoard.color[transitionSpot.vertex] = "blue"
        frontier.put(transitionSpot)

    # picCnt = graphSnapshot(myGameBoard,picCnt,fileNameFrontier)

    curRound+=1

successfulPath = findPath(start, goal, came_from, myGameBoard)
color_path(successfulPath, "orange", myGameBoard)

picCnt = graphSnapshot(myGameBoard,picCnt,fileNameFrontier)
