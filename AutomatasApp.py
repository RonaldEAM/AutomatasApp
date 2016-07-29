from kivy.app import App
from path import *
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import ObjectProperty, ListProperty, NumericProperty

class GridUI(GridLayout):
    status = ListProperty([0]*64)
    options = [1,2,3]
    color = {0: (.99, .89, .65, 1), 1: (.18, .8, .4, 1), 2: (.96, .28, .28, 1), 3: (.2, .6, .86, 1), 4: (.97, .58, .02, 1)}

    buttons_list = []
    button_inicio = ListProperty(None)
    button_final = ListProperty(None)
    button_obstaculos = ListProperty(None)
    nodes = []
    current_option = NumericProperty(1)
    def __init__(self, *args, **kwargs):
        super(GridUI, self).__init__(*args, **kwargs)
        for row in range(8):
            for column in range(8):
                node = Node(coords=(row,column))
                self.nodes.append(node)
                node.bind(on_press=self.button_pressed)
                self.add_widget(node)

    def button_pressed(self, button):
        if button not in self.buttons_list:
            self.buttons_list.append(button)

        row, column = button.coords

        status_index = 8*row + column
        already_taken = self.status[status_index]

        if already_taken not in self.options:
            if (self.current_option == 1 or self.current_option == 2) and self.current_option in self.status:
                for i in range(len(self.status)):
                    if self.status[i] == self.current_option:
                        self.status[i] = 0
                        c = i % 8
                        r = int(i / 8)
                        for b in self.buttons_list:
                            if b.coords == [r,c]:
                                b.background_color = self.color[0]
            self.status[status_index] = self.current_option
            button.background_color = self.color[self.current_option]

            if self.current_option == 1 and len(self.button_inicio) == 0:
                self.button_inicio.append(button.coords)
            if self.current_option == 1 and len(self.button_inicio) > 0:
                self.button_inicio[0] = button.coords

            if self.current_option == 2 and len(self.button_final) == 0:
                self.button_final.append(button.coords)
            if self.current_option == 2 and len(self.button_final) > 0:
                self.button_final[0] = button.coords

            if self.current_option == 3:
                self.button_obstaculos.append(button.coords)

            print(self.button_obstaculos)
        else:
            self.status[status_index] = 0
            button.background_color = self.color[0]
            if self.current_option == 3 and button.coords in self.button_obstaculos:
                self.button_obstaculos.remove(button.coords)

    def drawPath(self):
        grid = Grid(8,self.button_obstaculos)
        findPath = FindPath(grid,self.button_inicio[0],self.button_final[0])
        resultPath = findPath.result
        for node in self.nodes:
            for i in resultPath[:-1]:
                if node.coords == i:
                    node.background_color = self.color[4]

    def reset(self):
        self.status = [0]*64
        self.buttons_list = []
        self.button_inicio = []
        self.button_final = []
        self.button_obstaculos = []
        for node in self.nodes:
            node.background_color = self.color[0]


class Node(Button):
    coords = ListProperty([0,0])

class Principal(BoxLayout):
    def current_option(self,value):
        self.ids.grid.current_option = value

class AutomatasApp(App):
    def build(self):
        return Principal()

if __name__ == '__main__':
    AutomatasApp().run()
