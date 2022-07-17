

def evaluate_row(row: list):
    if " " in row:
        return "row not finished"
    elif "X" in row and not "O" in row:
        return "X"
    elif "O" in row and not "X" in row:
        return "O"
    else:
        return "draw"

def check_cell(cell: tuple, grid: list):
    try:
        row = int(cell[0])
        col = int(cell[1])
    except Exception:
        print("You should enter numbers!")
        return False
    else:
        if row not in (1, 2, 3) or col not in (1, 2, 3):
            print("Coordinates should be from 1 to 3!")
            return False
        elif grid[row - 1][col - 1] != " ":
            print("This cell is occupied! Choose another one!")
            return False
        else:
            return row, col


def is_grid_possible(grid: list):
    x_count = 0
    o_count = 0
    for row in grid:
        for value in row:
            if value == "X":
                x_count += 1
            elif value == "O":
                o_count += 1
    return (x_count - o_count) in (0, 1, -1)


def create_grid(data: list):
    grid = [[], [], []]
    for row in range(3):
        for col in range(3):
            grid[row].append(data[row * 3 + col])

    return grid


def empty_grid():
    return [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

def print_grid(grid: list):
    print("-" * 9)
    for row in grid:
        print("|", end="")
        for value in row:
            print(" ", value, sep="", end="")
        print(" |")
    print("-" * 9)

def evaluate_grid(grid: list):
    if not is_grid_possible(grid):
        return "Impossible"

    results = {"X": 0, "O": 0, "row not finished": 0, "draw": 0}

    for row in grid:
        results[evaluate_row(row)] += 1
    for i in range(3):
        col = []
        for j in range(3):
            col.append(grid[j][i])
        results[evaluate_row(col)] += 1
    diag_main, diag_sec = [], []
    for i in range(3):
        diag_main.append(grid[i][i])
        diag_sec.append(grid[i][2 - i])
    results[evaluate_row(diag_main)] += 1
    results[evaluate_row(diag_sec)] += 1
    if results["X"] + results["O"] > 1:
        return "Impossible"
    elif results["O"] > 0:
        return "O wins"
    elif results["X"] > 0:
        return "X wins"
    elif results["row not finished"] == 0:
        return "Draw"
    else:
        return "Game not finished"


grid = empty_grid()
print_grid(grid)
player = "X"
while True:
    turn = check_cell(tuple(input().split()), grid)
    if turn:
        grid[turn[0] - 1][turn[1] - 1] = player
        if player == "X":
            player = "O"
        else:
            player = "X"
        print_grid(grid)
        result = evaluate_grid(grid)
        if result != "Game not finished":
            print(result)
            break




