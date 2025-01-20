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
    def __init__(self, x1, x2, y1, y2, win):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win
    
    def draw(self, canvas):
        if(self.has_left_wall):
            left_line = Line(self._x1, self._x1, self._y1, self._y2)
            left_line.draw(canvas, "red")
        if(self.has_right_wall):
            right_line = Line(self._x2, self._x2, self._y1, self._y2)
            right_line.draw(canvas, "red")
        if(self.has_top_wall):
            top_line = Line(self._x1, self._x2, self._y1, self._y1)
            top_line.draw(canvas, "red")
        if(self.has_bottom_wall):
            bottom_line = Line(self._x1, self._x2, self._y2, self._y2)
            bottom_line.draw(canvas,"red")


win = Window(800, 600)
cell_one = Cell(100, 200, 100, 200, False)
cell_one.draw(win.canvas)
cell_two = Cell(300, 400, 300, 400, False)
cell_two.draw(win.canvas)
win.wait_for_close()