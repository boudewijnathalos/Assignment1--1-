############ CODE BLOCK 0 ################
# DO NOT CHANGE THIS CELL.
# THESE ARE THE ONLY IMPORTS YOU ARE ALLOWED TO USE:

import numpy as np
import copy

RNG = np.random.default_rng()

############ CODE BLOCK 11 ################
def set_grid(self, grid):
    """
    This method sets a new grid. This also can change the size of the sudoku.

    :param grid: A 2D numpy array that contains the digits for the grid.
    :type grid: ndarray[(Any, Any), int]
    """
    # Update the Sudoku grid with the new provided grid
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
    return ((row)//x)*x+((col)//x)

def get_box(self, box_id):
    """
    This method returns the "box_id" box.

    :param box_id: The index of the sudoku box.
    :type box_id: int
    :return: A box of the sudoku.
    :rtype: np.ndarray[(Any, Any), int]
    """
    x = int(np.sqrt(len(self.grid)))
    
    start_row = ((box_id) // x) * x
    start_col = ((box_id) % x) * x
    
    
    return self.grid[start_row:start_row + x, start_col:start_col + x]
    

############ CODE BLOCK 13 ################
@staticmethod
def is_set_correct(numbers):
    """
    This method checks if a set (row, column, or box) is correct according to the rules of a sudoku.
    In other words, this method checks if a set of numbers contains duplicate values between 1 and the size of the sudoku.
    Note, that multiple empty cells are not considered duplicates.

    :param numbers: The numbers of a sudoku's row, column, or box.
    :type numbers: np.ndarray[(Any, Any), int] or np.ndarray[(Any, ), int]
    :return: This method returns if the set is correct or not.
    :rtype: Boolean
    """
    flat_array = numbers.flatten()
    filled_in_numbers = flat_array[flat_array>0]
    return len(filled_in_numbers) == len(set(filled_in_numbers))
    
def check_cell(self, row, col):
    """
    This method checks if the cell, denoted by row and column, is correct according to the rules of sudoku.
    
    :param col: The column index that is tested.
    :type col: int
    :param row: The row index that is tested.
    :type row: int
    :return: This method returns if the cell, denoted by row and column, is correct compared to the rest of the grid.
    :rtype: boolean
    """
    row_ = self.get_row(row)
    col_ = self.get_col(col)
    box_index = self.get_box_index(row, col)
    box2 = self.get_box(box_index).flatten()

    return self.is_set_correct(row_) and self.is_set_correct(col_) and self.is_set_correct(box2)

def check_sudoku(self):
    """
    This method checks, for all rows, columns, and boxes, if they are correct according to the rules of a sudoku.
    In other words, this method checks, for all rows, columns, and boxes, if a set of numbers contains duplicate values between 1 and the size of the sudoku.
    Note, that multiple empty cells are not considered duplicates.

    Hint: It is not needed to check if every cell is correct to check if a complete sudoku is correct.

    :return: This method returns if the (partial) Sudoku is correct.
    :rtype: Boolean
    """
    a = self
    for i in range(len(self.grid)):
        if not self.is_set_correct(self.get_row(i)) or not self.is_set_correct(self.get_col(i)) or not self.is_set_correct(self.get_box(i)):
            return False
    return True 
    

    

############ CODE BLOCK 14 ################
def step(self, row=0, col=0, backtracking=False):
    print(self.grid)
    # If the end of the grid is reached and the Sudoku is valid, return True
    if row == len(self.grid) and self.check_sudoku: 
        return True 
        # If the current cell is not empty, proceed to the next step
    if self.grid[row][col] != 0:  
        return self.next_step(row, col, backtracking)
    # Try all possible numbers in the current empty cell
    for num in range(1, len(self.grid) + 1):  # Try all possible numbers
        self.grid[row][col] = num
        if (not backtracking or self.check_cell(row, col)) and self.next_step(row, col, backtracking):
            return True
        self.clean_up(row, col) # Reset the cell if the number doesn't fit
        
    return False  # Return False if no number fits in the current cell
    
def next_step(self, row, col, backtracking):
    # Calculate the next column index, wrapping to the next row if needed
    next_col = (col + 1) % len(self.grid)
    # Move to the next row if we are at the end of the current row
    next_row = row if col < len(self.grid) - 1 else row + 1
    # Continue with the next step of the solving process
    return self.step(next_row, next_col, backtracking)

def clean_up(self, row, col):
    self.grid[row][col] = 0  # Reset the cell to empty

def solve(self, backtracking):
    
    """
    Solve the sudoku using either recursive exhaustive search or backtracking.
    This is determined by the `backtracking` flag.
    
    :param backtracking: Determines if backtracking is used (True) or if exhaustive search without backtracking is used (False).
    :type backtracking: boolean, optional
    :return: This method returns if a correct solution for the whole sudoku was found.
    :rtype: boolean
    """
    return self.step(backtracking=backtracking)


############ END OF CODE BLOCKS, START SCRIPT BELOW! ################
