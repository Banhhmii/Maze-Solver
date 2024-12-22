from window import Window, Line, Point

def main():
    p1 = Point(3, 3)
    p2 = Point(200, 200)
    line = Line(p1, p2)
    win = Window(800, 600)
    win.draw_line(line, "black")
    win.wait_for_close()
    

main()