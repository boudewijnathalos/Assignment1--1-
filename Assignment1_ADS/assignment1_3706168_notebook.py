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
        filled_in_row = row_[row_>0]
        col_ = self.get_col(col)
        filled_in_col = col_[col_>0]
        box_index = self.get_box_index(row, col)
        box2 = self.get_box(box_index).flatten()
        filled_in_box = box2[box2>0]

        if len(filled_in_row) == len(set(filled_in_row)) and len(filled_in_col) == len(set(filled_in_col)) and len(filled_in_box) == len(set(filled_in_box)):
            return True
        else: 
            return False

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
        if row == len(self.grid):  # End of grid check, time to validate the whole grid
            print(self.grid)
            return self.check_sudoku()  # Check if the filled grid is a valid solution

        if self.grid[row][col] != 0:  # Skip filled cells
            return self.next_step(row, col, backtracking)
        
        for num in range(1, len(self.grid) + 1):  # Try all possible numbers
            self.grid[row][col] = num
            if self.next_step(row, col, backtracking):  # Move to the next cell
                return True
        self.clean_up(row, col)
        
        return False  # Continue trying numbers if no solution found yet

    def next_step(self, row, col, backtracking):
        next_col = (col + 1) % len(self.grid)
        next_row = row if col < len(self.grid) - 1 else row + 1
        return self.step(next_row, next_col, backtracking)

    def clean_up(self, row, col):
        self.grid[row][col] = 0  # Reset the cell to empty

    

    def solve(self, backtracking=False):
        """
        Solve the sudoku using a brute force approach.
        
        :return: This method returns if a correct solution for the whole sudoku was found.
        :rtype: boolean
        """

    
        return self.step(backtracking=backtracking)


############ END OF CODE BLOCKS, START SCRIPT BELOW! ################
