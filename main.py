from graphics import *

def main():
    win = Window(800, 600)
    pointA = Point(100, 100)
    pointB = Point(500, 500)
    pointC = Point(500, 100)
    line1 = Line(pointA, pointB)
    line2 = Line(pointA, pointC)
    line3 = Line(pointB, pointC)
    win.draw_line(line1, 'black')
    win.draw_line(line2, 'red')
    win.draw_line(line3, 'green')
    win.wait_for_close()
    

main()