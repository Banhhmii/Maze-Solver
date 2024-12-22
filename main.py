from graphics import Window, Line, Point, Cell

def main():
    p1 = Point(3, 3)
    p2 = Point(200, 200)
    line = Line(p1, p2)
    win = Window(800, 600)
    
    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225,225,255,255)

    c = Cell(win)
    c.has_right_wall = False
    c.draw(125,125,155,155)
    
    c = Cell(win)
    c.has_top_wall = False
    c.draw(325,325,355,355)
    
    #win.draw_line(line, "black")
    win.wait_for_close()
    

main()