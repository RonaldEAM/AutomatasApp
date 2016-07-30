class Directions:
    def __init__(self,path):
        self.cardinalList = []
        auxNode = 0
        for node in path:
            if (auxNode == 0):
                auxNode = node
            else:
                if (node[1] == auxNode[1]):
                    if (node[0] < auxNode[0]):
                        self.cardinalList.append('N')
                    else:
                        self.cardinalList.append('S')
                elif (node[0] == auxNode[0]):
                    if (node[1] < auxNode[1]):
                        self.cardinalList.append('O')
                    else:
                        self.cardinalList.append('E')
                elif (node[1] < auxNode[1]):
                    if (node[0] < auxNode[0]):
                        self.cardinalList.append('NO')
                    else:
                        self.cardinalList.append('SO')
                elif (node[1] > auxNode[1]):
                    if (node[0] < auxNode[0]):
                        self.cardinalList.append('NE')
                    else:
                        self.cardinalList.append('SE')
                auxNode = node
        print(self.cardinalList)

# directions = Directions([[0, 0], [0, 1], [1, 2], [2, 3], [3, 3], [4, 2], [5, 1], [5, 0], [4, 0]])
# print(directions.cardinalList)
