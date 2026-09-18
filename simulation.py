from grid import Grid

class Simulation: 
    def __init__(self,width, height, cell_size):
        self.grid = Grid(width, height, cell_size)
        #temporary grid that completes all updates then translates to become the og grid
        self.temp_grid = Grid(width, height, cell_size)
        self.rows = height // cell_size
        self.columns = width // cell_size
        self.run = False

    def draw(self, window):
        self.grid.draw(window)
     



    #scan neighbouring cells    
    def scanning(self, grid, row, column): 
        alive_cells = 0
        # [/][/][/]
        # [/][ ][/]
        # [/][/][/]
        offsets = [(1,0),(1,1),(0,1),(-1,1),(-1,0),(-1,-1),(0,-1),(1,-1)]   
        for offset in offsets:
            #if cell alive at border, wraps around grid
            new_row = (row + offset[0]) % self.rows
            new_column = (column + offset[1]) % self.columns
            if self.grid.cells[new_row][new_column] == 1: 
                alive_cells += 1

        return alive_cells

    def update(self): 
        if self.is_running():
            for row in range(self.rows):
                for column in range(self.columns):
                    alive_cells = self.scanning(self.grid, row, column) 
                    cell_value = self.grid.cells[row][column]

                    if cell_value == 1:
                        if alive_cells > 3 or alive_cells < 2:
                            self.temp_grid.cells[row][column] = 0
                        else: 
                            self.temp_grid.cells[row][column] = 1
                    else:
                        if alive_cells == 3: 
                            self.temp_grid.cells[row][column] = 1
                        else: 
                            self.temp_grid.cells[row][column] = 0
            for row in range(self.rows): 
                for column in range(self.columns): 
                    self.grid.cells[row][column] = self.temp_grid.cells[row][column]

    def is_running(self): 
        return self.run 

    def start(self): 
        self.run = True

    def edit_cells(self, row, column): 
        if self.run == False:
            self.grid.edit_cell(row,column)
