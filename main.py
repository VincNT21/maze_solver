from graphics import Window
from cell import Cell

def main():
    win = Window(800, 600)
    cell1 = Cell(win)
    cell1.has_bottom_wall = False
    cell1.draw(10, 50, 10, 50)
    cell2 = Cell(win)
    cell2.has_top_wall = False
    cell2.draw(10, 50, 52, 92)
    cell1.draw_move(cell2)
    win.wait_for_close()
    

main()