from graphics import Window, Line, Point, Cell

def main():
    p1 = Point(3, 3)
    p2 = Point(200, 200)
    line = Line(p1, p2)
    win = Window(800, 600)
    
    c = Cell(win)
    c.has_right_wall = False
    c.draw(50,50,100,100)

    c1 = Cell(win)
    c1.has_left_wall = False
    c1.has_bottom_wall = False
    c1.draw(100,50,150,100)
    
    c.draw_move(c1)
    
    c = Cell(win)
    c.has_top_wall = False
    c.draw(325,325,355,355)
    
    #win.draw_line(line, "black")
    win.wait_for_close()
    

main()