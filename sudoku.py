from collections import deque
import copy

N = 9

backtrack_calls = 0
backtrack_failures = 0

# Read board from file
def read_board(filename):
    board = []
    with open(filename, 'r') as f:
        for line in f:
            board.append([int(x) for x in line.strip()])
    return board

# Print board
def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

# Check validity
def is_valid(board, row, col, num):
    for i in range(N):
        if board[row][i] == num or board[i][col] == num:
            return False

    sr, sc = 3*(row//3), 3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[sr+i][sc+j] == num:
                return False

    return True

# Domain of a cell
def get_domain(board, row, col):
    domain = set(range(1,10))

    for i in range(N):
        domain.discard(board[row][i])
        domain.discard(board[i][col])

    sr, sc = 3*(row//3), 3*(col//3)
    for i in range(3):
        for j in range(3):
            domain.discard(board[sr+i][sc+j])

    return domain

# Find empty cell
def find_empty(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                return i, j
    return None

# AC-3 helpers
def get_neighbors(row, col):
    neighbors = set()

    for i in range(N):
        if i != col:
            neighbors.add((row, i))
        if i != row:
            neighbors.add((i, col))

    sr, sc = 3*(row//3), 3*(col//3)
    for i in range(3):
        for j in range(3):
            r, c = sr+i, sc+j
            if (r, c) != (row, col):
                neighbors.add((r, c))

    return neighbors

def revise(domains, xi, xj):
    revised = False
    if len(domains[xj]) == 1:
        val = next(iter(domains[xj]))
        if val in domains[xi]:
            domains[xi].remove(val)
            revised = True
    return revised

def ac3(domains):
    queue = deque()

    for xi in domains:
        for xj in get_neighbors(*xi):
            queue.append((xi, xj))

    while queue:
        xi, xj = queue.popleft()

        if revise(domains, xi, xj):
            if len(domains[xi]) == 0:
                return False
            for xk in get_neighbors(*xi):
                if xk != xj:
                    queue.append((xk, xi))
    return True

# Convert board to domains
def init_domains(board):
    domains = {}
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                domains[(i,j)] = get_domain(board, i, j)
            else:
                domains[(i,j)] = {board[i][j]}
    return domains

# Forward Checking + Backtracking
def backtrack(board, domains):
    global backtrack_calls, backtrack_failures
    backtrack_calls += 1

    empty = find_empty(board)
    if not empty:
        return True

    row, col = empty

    for val in domains[(row, col)]:
        if is_valid(board, row, col, val):
            board[row][col] = val

            new_domains = copy.deepcopy(domains)
            new_domains[(row, col)] = {val}

            if ac3(new_domains):
                if backtrack(board, new_domains):
                    return True

            board[row][col] = 0

    backtrack_failures += 1
    return False


# MAIN
if __name__ == "__main__":
    board = read_board("easy.txt")

    domains = init_domains(board)

    if ac3(domains) and backtrack(board, domains):
        print("Solved Sudoku:\n")
        print_board(board)
    else:
        print("No solution found")

    print("\nBacktrack Calls:", backtrack_calls)
    print("Backtrack Failures:", backtrack_failures)