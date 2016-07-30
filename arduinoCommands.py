from directions import *

class Commands:
    def __init__(self,path):
        directions = Directions(path).cardinalList
        self.commands = ''
        directions_dict = {'forward':'a','left':'b','stop':'c','right':'d','leftDiagonal':'e','rightDiagonal':'f'}
        auxDirection = 0
        for direction in directions:
            if (auxDirection == 0):
                self.commands +=  directions_dict['forward']
                auxDirection = direction
            else:
                if (auxDirection == 'N'):
                    if (direction == 'O'):
                        self.commands +=  directions_dict['left']
                    elif (direction == 'NO'):
                        self.commands +=  directions_dict['leftDiagonal']
                    elif (direction == 'N'):
                        self.commands +=  directions_dict['forward']
                    elif (direction == 'NE'):
                        self.commands +=  directions_dict['rightDiagonal']
                    elif (direction == 'E'):
                        self.commands +=  directions_dict['right']
                elif (auxDirection == 'NE'):
                    if (direction == 'NO'):
                        self.commands +=  directions_dict['left']
                    elif (direction == 'N'):
                        self.commands +=  directions_dict['leftDiagonal']
                    elif (direction == 'NE'):
                        self.commands +=  directions_dict['forward']
                    elif (direction == 'E'):
                        self.commands +=  directions_dict['rightDiagonal']
                    elif (direction == 'SE'):
                        self.commands +=  directions_dict['right']
                elif (auxDirection == 'E'):
                    if (direction == 'N'):
                        self.commands +=  directions_dict['left']
                    elif (direction == 'NE'):
                        self.commands +=  directions_dict['leftDiagonal']
                    elif (direction == 'E'):
                        self.commands +=  directions_dict['forward']
                    elif (direction == 'SE'):
                        self.commands +=  directions_dict['rightDiagonal']
                    elif (direction == 'S'):
                        self.commands +=  directions_dict['right']
                elif (auxDirection == 'SE'):
                    if (direction == 'NE'):
                        self.commands +=  directions_dict['left']
                    elif (direction == 'E'):
                        self.commands +=  directions_dict['leftDiagonal']
                    elif (direction == 'SE'):
                        self.commands +=  directions_dict['forward']
                    elif (direction == 'S'):
                        self.commands +=  directions_dict['rightDiagonal']
                    elif (direction == 'SO'):
                        self.commands +=  directions_dict['right']
                elif (auxDirection == 'S'):
                    if (direction == 'E'):
                        self.commands +=  directions_dict['left']
                    elif (direction == 'SE'):
                        self.commands +=  directions_dict['leftDiagonal']
                    elif (direction == 'S'):
                        self.commands +=  directions_dict['forward']
                    elif (direction == 'SO'):
                        self.commands +=  directions_dict['rightDiagonal']
                    elif (direction == 'O'):
                        self.commands +=  directions_dict['right']
                elif (auxDirection == 'SO'):
                    if (direction == 'SE'):
                        self.commands +=  directions_dict['left']
                    elif (direction == 'S'):
                        self.commands +=  directions_dict['leftDiagonal']
                    elif (direction == 'SO'):
                        self.commands +=  directions_dict['forward']
                    elif (direction == 'O'):
                        self.commands +=  directions_dict['rightDiagonal']
                    elif (direction == 'NO'):
                        self.commands +=  directions_dict['right']
                elif (auxDirection == 'O'):
                    if (direction == 'S'):
                        self.commands +=  directions_dict['left']
                    elif (direction == 'SO'):
                        self.commands +=  directions_dict['leftDiagonal']
                    elif (direction == 'O'):
                        self.commands +=  directions_dict['forward']
                    elif (direction == 'NO'):
                        self.commands +=  directions_dict['rightDiagonal']
                    elif (direction == 'N'):
                        self.commands +=  directions_dict['right']
                elif (auxDirection == 'NO'):
                    if (direction == 'SO'):
                        self.commands +=  directions_dict['left']
                    elif (direction == 'O'):
                        self.commands +=  directions_dict['leftDiagonal']
                    elif (direction == 'NO'):
                        self.commands +=  directions_dict['forward']
                    elif (direction == 'N'):
                        self.commands +=  directions_dict['rightDiagonal']
                    elif (direction == 'NE'):
                        self.commands +=  directions_dict['right']
                auxDirection = direction
        self.commands +=  directions_dict['stop']
        print(self.commands)

# commands = Commands([[0, 0], [0, 1], [1, 2], [2, 3], [3, 3], [4, 2], [5, 1], [5, 0], [4, 0]]).commands
# print(commands)
