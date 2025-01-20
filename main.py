import time
from tkinter import Tk, BOTH, Canvas
class Window:
    def __init__(self, width, height):
        self.root = Tk()
        self.root.title("Maze Solver")
        
        # Create a Canvas widget and save it as a data member
        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack()
        
        self.is_running = False

    def start(self):
        self.is_running = True
        self.root.mainloop()

    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.is_running = True
        while(self.is_running):
            self.redraw()
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Line:
    def __init__(self, x1, x2, y1, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    def draw(self, canvas, fill_color):
        canvas.create_line(self.x1, self.y1, self.x2, self.y2, fill = fill_color, width = 2)

class Cell:
    def __init__(self, x1, x2, y1, y2, window):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = window
    
    def draw(self):
        if(self.has_left_wall):
            left_line = Line(self._x1, self._x1, self._y1, self._y2)
            left_line.draw(self._win.canvas, "white")
        if(self.has_right_wall):
            right_line = Line(self._x2, self._x2, self._y1, self._y2)
            right_line.draw(self._win.canvas, "white")
        if(self.has_top_wall):
            top_line = Line(self._x1, self._x2, self._y1, self._y1)
            top_line.draw(self._win.canvas, "white")
        if(self.has_bottom_wall):
            bottom_line = Line(self._x1, self._x2, self._y2, self._y2)
            bottom_line.draw(self._win.canvas, "white")
    
    def draw_move(self, to_cell, undo=False):
        x1 = (self._x1 + self._x2) / 2
        y1 = (self._y1 + self._y2) / 2
        x2 = (to_cell._x1 + to_cell._x2) / 2
        y2 = (to_cell._y1 + to_cell._y2) / 2
        new_line = Line(x1, x2, y1, y2)
        color = "red" if undo == False else "gray"
        new_line.draw(self._win.canvas, color)

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.window = win

    def _create_cells(self):
        self._cells = []

        for i in range(self.num_rows):
            row = [] 
            for j in range(self.num_cols): 
                x1 = self.x1 + (j * self.cell_size_x)
                y1 = self.y1 + (i * self.cell_size_y)

                x2 = x1 + self.cell_size_x
                y2 = y1 + self.cell_size_y

                cell = Cell(x1, x2, y1, y2, self.window)

                row.append(cell)
                self._draw_cell(cell)
                
            self._cells.append(row)

    def _draw_cell(self, cell):
        cell.draw()
        self._animate()

    def _animate(self):
        self.window.redraw()
        time.sleep(0.05)


win = Window(800, 600)
test_maze = Maze(10, 10, 10, 10, 30, 30, win)
test_maze._create_cells()
win.wait_for_close()