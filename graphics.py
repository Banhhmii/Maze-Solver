from tkinter import Tk, BOTH, Canvas

class Window:
    def __init__(self, width, height):
        self.__root = Tk()
        self.__root.title("Maze Solver")
        self.__root.protocol("WM_DELETE_WINDOW", self.close())
        self.__canvas = Canvas(self.__root, height=height, width=width, bg="white")
        self.__canvas.pack(fill=BOTH, expand=1)
        self.__running = False
    
    def redraw(self):
        self.__root.update_idletasks()
        self.__root.update()
        
    def draw_line(self, line, fill_color="black"):
        line.draw(self.__canvas, fill_color)       
    
    def wait_for_close(self):
        self.__running = True
        while self.__running:
            self.redraw()
    
    def close(self):
        self.__running = False
         

class Point:
    def __init__(self, x, y):
        self.x = x 
        self.y = y
        
class Line:
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
    
    def draw(self, canvas, fill_color="black"):
        canvas.create_line(self.point1.x, self.point1.y, self.point2.x, self.point2.y, fill=fill_color, width=2)
        
class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self._win = win
        
    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
    
        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1,y2))
            self._win.draw_line(line, "white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2,y2))
            self._win.draw_line(line, "white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2,y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2,y1))
            self._win.draw_line(line, "white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2,y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2,y2))
            self._win.draw_line(line, "white")
    
    def draw_move(self, to_cell, undo=False):
            length1 = abs(self._x1 - self._x2) // 2
            x1_center = length1 + self._x1
            y1_center = length1 + self._y1
            
            length2 = abs(to_cell._x1 - to_cell._x2) // 2
            x2_center = length2 + to_cell._x1
            y2_center = length2 + to_cell._y1
            
            full_color = "red"
            if undo:
                full_color = "gray"
            line = Line(Point(x1_center, y1_center), Point(x2_center, y2_center))
            self._win.draw_line(line, full_color)