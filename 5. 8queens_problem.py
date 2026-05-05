N = 8

# Print solution
def print_board(board):
    for row in board:
        print(" ".join(row))
    print()

# Check if safe
def is_safe(board, row, col):
    # Check column
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    # Check left diagonal
    i, j = row-1, col-1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    # Check right diagonal
    i, j = row-1, col+1
    while i >= 0 and j < N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True

# Solve using backtracking
def solve(board, row):
    if row == N:
        print_board(board)
        return True  # print one solution

    for col in range(N):
        if is_safe(board, row, col):
            board[row][col] = 'Q'

            if solve(board, row + 1):
                return True

            board[row][col] = '.'  # backtrack

    return False


# Initialize board
board = [['.' for _ in range(N)] for _ in range(N)]

# Run
solve(board, 0)
