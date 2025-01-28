from graphics import Window
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(50, 50, 5, 6, 40, 40, win)
    win.wait_for_close()
    

main()