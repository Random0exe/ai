def solve_n_queens(n):
    solutions = []
    board = [['.' for _ in range(n)] for _ in range(n)]
    backtrack(board, 0, solutions)
    return solutions

def backtrack(board, row, solutions):
    if row == len(board):
        solutions.append([''.join(row) for row in board])
        return
    
    for col in range(len(board)):
        if is_valid(board, row, col):
            board[row][col] = 'Q'
            backtrack(board, row + 1, solutions)
            board[row][col] = '.'


def is_valid(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check if there is a queen in the upper left diagonal
    i, j = row - 1, col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper right diagonal
    i, j = row - 1, col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

n = int(input("Enter n: "))
solutions = solve_n_queens(n)
print(f"Number of solutions for {n}-queens: {len(solutions)}")
for i, solution in enumerate(solutions):
    print(f"Solution {i + 1}:")
    for row in solution:
        print(row)
    print()
