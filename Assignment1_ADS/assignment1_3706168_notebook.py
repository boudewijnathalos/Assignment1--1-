############ CODE BLOCK 0 ################
# DO NOT CHANGE THIS CELL.
# THESE ARE THE ONLY IMPORTS YOU ARE ALLOWED TO USE:

import numpy as np
import copy

RNG = np.random.default_rng()

############ CODE BLOCK 10 ################
class Sudoku():
    """
    This class creates sudoku objects which can be used to solve sudokus. 
    A sudoku object can be any size grid, as long as the square root of the size is a whole integer.
    To indicate that a cell in the sudoku grid is empty we use a zero.
    A sudoku object is initialized with an empty grid of a certain size.

    Attributes:
        :param self.grid: The sudoku grid containing all the digits.
        :type self.grid: np.ndarray[(Any, Any), int]  # The first type hint is the shape, and the second one is the dtype. 
        :param self.size: The width/height of the sudoku grid.
        :type self.size: int
    """
    def __init__(self, size=49):
        self.grid = np.zeros((size, size))
        self.size = size
        
    def is_valid_sudoku_size(self, size):
        for i in range(1, size + 1):
            if i * i == size:
                return True
            elif i * i > size:
                break
        return False
    
    def __repr__(self):
        if self.is_valid_sudoku_size(self.size):
            string_grid = ""
            for i, row in enumerate(self.grid):
                if i % int(np.sqrt(self.size)) == 0 and i != 0:
                    string_grid += "\n"  
                for j, val in enumerate(row):
                    if j % int(np.sqrt(self.size)) == 0 and j != 0:
                        string_grid += "| "  
                    string_grid += f"{int(val)} "
                string_grid += "\n" 
            return string_grid
        else:
            return 'Not a valid sudoku size'

############ CODE BLOCK 11 ################
    def set_grid(self, grid):
        """
        This method sets a new grid. This also can change the size of the sudoku.

        :param grid: A 2D numpy array that contains the digits for the grid.
        :type grid: ndarray[(Any, Any), int]
        """
        
        self.grid = grid
        return grid

############ CODE BLOCK 12 ################
    def get_row(self, row_id):
        """
        This method returns the row with index row_id.

        :param row_id: The index of the row.
        :type row_id: int
        :return: A row of the sudoku.
        :rtype: np.ndarray[(Any,), int]
        """
        
        return self.grid[row_id]

    def get_col(self, col_id):
        """
        This method returns the column with index col_id.

        :param col_id: The index of the column.
        :type col_id: int
        :return: A row of the sudoku.
        :rtype: np.ndarray[(Any,), int]
        """
        return self.grid[:, col_id]
       

    def get_box_index(self, row, col):
        """
        This returns the box index of a cell given the row and column index.
        
        :param col: The column index.
        :type col: int
        :param row: The row index.
        :type row: int
        :return: This returns the box index of a cell.
        :rtype: int
        """
        x = int(np.sqrt(len(self.grid)))
        return ((row)//2)*2+((col)//2)

    def get_box(self, box_id):
        """
        This method returns the "box_id" box.

        :param box_id: The index of the sudoku box.
        :type box_id: int
        :return: A box of the sudoku.
        :rtype: np.ndarray[(Any, Any), int]
        """
        x = int(np.sqrt(len(self.grid)))
        
        start_row = ((box_id-1) // x) * x
        start_col = ((box_id-1) % x) * x
        
        
        return self.grid[start_row:start_row + x, start_col:start_col + x]
        


############ END OF CODE BLOCKS, START SCRIPT BELOW! ################
