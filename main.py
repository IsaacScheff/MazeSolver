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
    def __init__(self, point_a, point_b):
        self.point_a = point_a
        self.point_b = point_b

    def draw(self, canvas, fill_color):
        canvas.create_line(self.point_a.x, self.point_a.y, self.point_b.x, self.point_b.y, fill = fill_color, width = 2)

win = Window(800, 600)
point_one = Point(100, 100)
point_two = Point(400, 400)
test_line = Line(point_one, point_two)
win.draw_line(test_line, "red")
win.wait_for_close()