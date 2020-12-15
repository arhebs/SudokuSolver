# -*- coding: utf-8 -*-
"""
Created on Tue Dec 15 14:53:50 2020

@author: Shalom
"""

def find_next_empty(puzzle):
   
    for r in range(9):
        for c in range(9): 
            if puzzle[r][c] == 0:
                return r, c

    return None, None  

def is_valid(puzzle, guess, row, col):
  
    row_vals = puzzle[row]
    if guess in row_vals:
        return False 

    
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False

    row_start = (row // 3) * 3 
    col_start = (col // 3) * 3

    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False

    return True

def solve_sudoku(puzzle):
    if row is None:
        return True 
    
    for guess in range(1, 10): 
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        
        puzzle[row][col] = 0

    return False

    
if __name__ == '__main__':
    
    example_board = []

    with open ("data.txt") as textfile:
        for line in textfile:
            data = [int(item.strip()) for item in line.split(" ")]
            example_board.append(data)
    
    solve_sudoku(example_board)
    print(example_board)