from numpy import arange, array, empty, ndenumerate, vectorize
from graph_tool.all import *
from queue import PriorityQueue
from random import randrange
import time

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
    edge_weights = graphMain.new_edge_property('double')
    edge_colors = graphMain.new_edge_property("string")

    def __init__(self):
        totalSpots = self.width*self.height
        self._boardSpots = arange(totalSpots).reshape(self.width, self.height)

        self.lattice = array( [ [BoardSpot(i,j) for i in range(self.height)] for j in range(self.width) ],
                                    dtype=object)
        self.connect_spots()

    def connect_spots(self):
        width, height = self.lattice.shape
        for (row, col), val in ndenumerate(self.lattice):
            self.lattice[row][col].vertex = self.graphMain.add_vertex()

        for (row, col), val in ndenumerate(self.lattice):
            neighbors = self.find_neighbors(row,col)
            for neighbor in neighbors:
                if neighbor.vertex is not None:
                    if ( neighbor.vertex not in self.lattice[row][col].vertex.all_neighbours() ):
                        newEdge = self.graphMain.add_edge(self.lattice[row][col].vertex, neighbor.vertex)
                        # print("NewEdge: ", newEdge)
                        # print("NewEdgeType: ", type(newEdge))
                        newWeight = randrange(0, 2)
                        # newWeight = randrange(0, 10)
                        if newWeight == 0:
                            newWeight = 10
                        self.edge_weights[newEdge] = newWeight
                        if newWeight > 5:
                            self.edge_colors [newEdge] = "purple"
                        else:
                            self.edge_colors [newEdge] = "green"


    def print_spots(self):
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

def find_path(start, goal, came_from, gameBoard):
    current = goal
    path = [current]
    while current != start:
        current = came_from[current]
        path.append(current)

    return path

def get_edge_from_indices(source, target, myGameBoard):
    for edge in myGameBoard.graphMain.edges():
        if int(source.vertex) == int(edge.source()) and int(target.vertex) == int(edge.target()):
            return edge
    return None

def color_path(path,color, gameBoard):
    for spot in path:
        gameBoard.color[spot.vertex] = color

def graph_snapshot(myGameBoard,picCnt,fileName):
    result = graph_draw(
            myGameBoard.graphMain, 
            # edge_text=myGameBoard.edge_weights,
            # edge_text_color="white",
            # vertex_text=myGameBoard.graphMain.vertex_index, 
            # eweight=myGameBoard.edge_weights,
            edge_color=myGameBoard.edge_colors,
            vertex_font_size=4, 
            output_size=(1200, 1200), 
            vertex_size=15, 
            vertex_color=myGameBoard.color, 
            vertex_fill_color=myGameBoard.color, 
            pos=myGameBoard.pos, 
            #Remove output parameter for interactive window
            output=fileName+format(picCnt, '02d')+".png"
            )
    print(result)
    return picCnt + 1

myGameBoard = GameBoard()
startIdx = 5
start = myGameBoard.lattice[startIdx][startIdx]
goal = myGameBoard.lattice[startIdx][startIdx+17]

came_from = {}
cost_so_far = {}
frontier = PriorityQueue()
frontier.put((0, time.time(), start))


came_from[start] = None
cost_so_far[start] = 0

picCnt=0

myGameBoard.reset_colors()
fileNameMain="board"
fileNameFrontier="frontier"

curRound = 0
# while curRound < numrounds and goal not in came_from:
while curRound < numrounds and goal not in came_from:
    myGameBoard.reset_colors()
    nextFrontier = PriorityQueue()

    while not frontier.empty():
        target = frontier.get()[2]
        row = target.y
        col = target.x

        for neighbor in myGameBoard.find_neighbors(row,col):
            new_cost = cost_so_far[target] 
            targetEdge = get_edge_from_indices(target, neighbor, myGameBoard)
            if targetEdge is not None:
                new_cost = new_cost + myGameBoard.edge_weights[targetEdge]

            if neighbor not in cost_so_far or new_cost < cost_so_far[neighbor]:
                # new_cost = cost_so_far[target] + graph.cost(target, neighbor)
                cost_so_far[neighbor] = new_cost
                priority = new_cost
                nextFrontier.put((priority, time.time(), neighbor))
                came_from[neighbor] = target

    for spot in came_from:
        myGameBoard.color[spot.vertex] = "grey"

    while not nextFrontier.empty():
        transitionSpot = nextFrontier.get()[2]
        myGameBoard.color[transitionSpot.vertex] = "blue"
        frontier.put((1, time.time(), transitionSpot))

    # picCnt = graph_snapshot(myGameBoard,picCnt,fileNameFrontier)

    curRound+=1

successfulPath = find_path(start, goal, came_from, myGameBoard)
color_path(successfulPath, "orange", myGameBoard)

picCnt = graph_snapshot(myGameBoard,picCnt,fileNameFrontier)

# get_edge_from_indices(623, 624, myGameBoard)

# for edge in myGameBoard.graphMain.edges():
#     print("Edge: ", edge)
