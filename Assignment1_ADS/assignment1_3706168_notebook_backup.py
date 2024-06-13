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
        # flattening the box for checking for doubles
        flat_array = numbers.flatten()
        # selecting only the nonzeros
        filled_in_numbers = flat_array[flat_array>0]
        # checking for doubles
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
        # selecting rows, columns and boxes
        row_ = self.get_row(row)
        col_ = self.get_col(col)
        box_index = self.get_box_index(row, col)
        box2 = self.get_box(box_index).flatten()
        # selecting only the nonzeros
        filled_in_col = col_[col_>0]
        filled_in_row = row_[row_>0]
        filled_in_box = box2[box2>0]
        # checking for doubles
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
        # checking every number of row, column or box if the value is correct
        for i in range(len(self.grid)):
            if not self.is_set_correct(self.get_row(i)) or not self.is_set_correct(self.get_col(i)) or not self.is_set_correct(self.get_box(i)):
                return False
        return True
        

        

############ CODE BLOCK 14 ################
    def step(self, row=0, col=0, backtracking=False):
        print(self.grid)
        if row == len(self.grid) and self.check_sudoku: 
            return True 

        if self.grid[row][col] != 0:  
            return self.next_step(row, col, backtracking)
        
        for num in range(1, len(self.grid) + 1):  # Try all possible numbers
            self.grid[row][col] = num
            if (not backtracking or self.check_cell(row, col)) and self.next_step(row, col, backtracking):
                return True
            self.clean_up(row, col)
            
        return False  
        
    def next_step(self, row, col, backtracking):
        next_col = (col + 1) % len(self.grid)
        next_row = row if col < len(self.grid) - 1 else row + 1
        return self.step(next_row, next_col, backtracking)

    def clean_up(self, row, col):
        self.grid[row][col] = 0  # Reset the cell to empty

    def solve(self, backtracking):
        print("lse")
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
