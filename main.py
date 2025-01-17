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

win = Window(800, 600)
win.wait_for_close()