#!/usr/bin/python3
'''
The N queens puzzle
'''
import sys


def is_safe(board, row, col):
    """Check if it's safe to place a queen at board[row][col]."""
    for i in range(row):
        if board[i] == col or \
           board[i] - i == col - row or \
           board[i] + i == col + row:
            return False
    return True


def solve_nqueens(N):
    """Solve the N queens puzzle and print all solutions."""
    def backtrack(row=0, current_solution=[]):
        if row == N:
            solutions.append(current_solution[:])
            return
        for col in range(N):
            if is_safe(current_solution, row, col):
                current_solution.append(col)
                backtrack(row + 1, current_solution)
                current_solution.pop()
    
    solutions = []
    backtrack()
    
    # Print all solutions in the required format
    for solution in solutions:
        print([[i, solution[i]] for i in range(N)])


if __name__ == "__main__":
    # Ensure the correct number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    # Validate that N is an integer and >= 4
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    # Solve the N queens problem
    solve_nqueens(N)
