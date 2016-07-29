class Node:
    def __init__(self,walkable,position):
        self.walkable = walkable
        self.position = position
        self.gCost = 0
        self.hCost = 0
        self.fCost = self.gCost + self.hCost
        self.parent = None

class Grid:
    def __init__(self,gridSize,blocks):
        self.blocks = blocks
        self.gridSize = gridSize
        self.grid = [[Node(True,[x,y]) for x in range(self.gridSize)] for y in range(self.gridSize)]
        for block in self.blocks:
            self.grid[block[1]][block[0]] = Node(False,block)

    def returnNode(self,position):
        positionX = position[0]
        positionY = position[1]
        return self.grid[positionY][positionX]

    def getNeighbors(self, node):
        neighbors = []
        for x in range(-1,2):
            for y in range(-1,2):
                if(x == 0 and y == 0):
                    continue
                checkX = node.position[0] + x
                checkY = node.position[1] + y
                if (checkX >= 0 and checkX < self.gridSize and checkY >= 0 and checkY < self.gridSize):
                    neighbors.append(self.grid[checkY][checkX])
        return neighbors

    def drawGrid(self,path,option):
        if (option == 0):
            grid = [['.']*self.gridSize for i in range(self.gridSize)]
            grid[path.startPos[1]][path.startPos[0]] = 'I'
            grid[path.targetPos[1]][path.targetPos[0]] = 'F'
            for i in self.blocks:
                grid[i[1]][i[0]] = 'X'
            for i in grid:
                print(i)
        else:
            grid = [['.']*self.gridSize for i in range(self.gridSize)]
            grid[path.startPos[1]][path.startPos[0]] = 'I'
            grid[path.targetPos[1]][path.targetPos[0]] = 'F'
            for i in self.blocks:
                grid[i[1]][i[0]] = 'X'
            for i in path.result:
                grid[i[1]][i[0]] = '#'
            for i in grid:
                print(i)

class FindPath:
    def __init__(self,grid,startPos,targetPos):
        self.startPos = startPos
        self.targetPos = targetPos
        self.startNode = grid.returnNode(self.startPos)
        self.targetNode = grid.returnNode(self.targetPos)
        openSet = []
        closedSet = []
        openSet.append(self.startNode)
        while(len(openSet) > 0):
            currentNode = openSet[0]
            for i in range(1,len(openSet)):
                if (openSet[i].fCost < currentNode.fCost or openSet[i].fCost == currentNode.fCost and openSet[i].hCost < currentNode.hCost):
                    currentNode = openSet[i]
            openSet.remove(currentNode)
            closedSet.append(currentNode)
            if (currentNode == self.targetNode):
                self.result = retracePath(self.startNode,self.targetNode)
                break
            for neighbor in grid.getNeighbors(currentNode):
                if (not neighbor.walkable or neighbor in closedSet):
                    continue
                newMovementCostToNeighbor = currentNode.gCost + getDistance(currentNode,neighbor)
                if (newMovementCostToNeighbor < neighbor.gCost or neighbor not in openSet):
                    neighbor.gCost = newMovementCostToNeighbor
                    neighbor.hCost = getDistance(neighbor,self.targetNode)
                    neighbor.fCost = neighbor.gCost + neighbor.hCost
                    neighbor.parent = currentNode
                    if (neighbor not in openSet):
                        openSet.append(neighbor)

def retracePath(startNode,endNode):
    path = []
    currentNode = endNode
    while (currentNode != startNode):
        path.append(currentNode.position)
        currentNode = currentNode.parent
    path = path[::-1]
    return path

def getDistance(nodeA,nodeB):
    dstX = abs(nodeA.position[0]-nodeB.position[0])
    dstY = abs(nodeA.position[1]-nodeB.position[1])
    if (dstX > dstY):
        return 14*dstY + 10*(dstX - dstY)
    else:
        return 14*dstX + 10*(dstY - dstX)

# grid1 = Grid(9,[[2,0],[2,1],[2,2],[2,3],[2,4],[2,5],[2,6],[2,7],[4,8],[4,7],[4,6],[4,5]]) #gridSize, Blocks
# algoritmo = FindPath(grid1,[6,6],[0,1]) #grid, start, end
# grid1.drawGrid(algoritmo,0) #findPath, 0=Sin resolver 1=Resuelto
