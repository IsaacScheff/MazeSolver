from maze import Maze, Window

def main():
    win = Window(800, 600)
    test_maze = Maze(10, 10, 10, 10, 30, 30, win)
    test_maze._create_cells()
    test_maze._break_entrance_and_exit()
    win.wait_for_close()

main()