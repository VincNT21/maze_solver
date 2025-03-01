from graphics import Window
from cell import Cell
from maze import Maze

def main():
    screen_x = 800
    screen_y = 600
    num_rows = 5
    nums_cols = 5
    margin = 50
    cell_size_x = (screen_x - 2 * margin) / nums_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, nums_cols, cell_size_x, cell_size_y, win)
    print("maze created")
    
    
    win.wait_for_close()
    

main()