from graphics import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._cells = []
        self.seed = None
        
        if seed:
            random.seed(seed)
        
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()

    def _create_cells(self):
        for i in range(self.num_cols):
            columns = []
            for j in range(self.num_rows):
                columns.append(Cell(self.win))
            self._cells.append(columns)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i,j)
    
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1 = self.x1 + i * self.cell_size_x
        y1 = self.y1 + j * self.cell_size_y
        x2 = x1 + self.cell_size_x
        y2 = y1 + self.cell_size_y
        self._cells[i][j].draw(x1, y1, x2, y2)
        self._animate()
    
    def _animate(self):
        if self.win is None:
            return
        self.win.redraw()
        time.sleep(0.03)
        
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self.num_cols - 1][self.num_rows - 1].has_bottom_wall = False
        self._draw_cell(self.num_cols - 1, self.num_rows - 1)
        
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        while True:
            next_list = []
            
            #decide which cells to visit
            #left cell
            if i > 0 and not self._cells[i - 1][j].visited:
                next_list.append((i - 1, j))
            #right cell
            if i < self.num_cols - 1 and not self._cells[i + 1][j].visited:
                next_list.append((i + 1, j))
            #top cell
            if j > 0 and not self._cells[i][j - 1].visited:
                next_list.append((i, j - 1))
            #bottom cell
            if j < self.num_rows - 1 and not self._cells[i][j + 1].visited:
                next_list.append((i, j + 1))
            
            if len(next_list) == 0:
                self._draw_cell(i, j)
                return

            #randomly choose a direction to go next
            random_direction = random.randrange(len(next_list))
            next_cell = next_list[random_direction]
            
            #knock down the walls that leads to the next cell
            #left cell
            if next_cell[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            #right cell
            if next_cell[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            #top cell
            if next_cell[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
            #bottom cell
            if next_cell[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            
            self._break_walls_r(next_cell[0], next_cell[1])
            
    def _reset_cells_visited(self):
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._cells[i][j].visited = False
                
    def solve(self):
        return self.solve_r(0, 0)

    def solve_r(self, i, j):
        self._animate()
        #current cell
        self._cells[i][j].visited = True
        #we are done if we are at the end
        if i == self.num_cols - 1 and j == self.num_rows - 1:
            return True
        
        #go left if there is no wall and it has not been visited
        if i > 0 and not self._cells[i][j].has_left_wall and not self._cells[i - 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self.solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
                
        #go right if there is no wall and it has not been visited
        if i < self.num_cols - 1 and not self._cells[i][j].has_right_wall and not self._cells[i + 1][j].visited:
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self.solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        
        #go up if there is no wall and it has not been visited
        if j > 0 and not self._cells[i][j].has_top_wall and not self._cells[i][j - 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self.solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
                
        #go down if there is no wall and it has not been visited
        if j < self.num_rows - 1 and not self._cells[i][j].has_bottom_wall and not self._cells[i][j + 1].visited:
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self.solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)
        
        return False

        
            