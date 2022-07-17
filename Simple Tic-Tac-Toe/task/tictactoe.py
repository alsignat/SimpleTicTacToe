

def evaluate_row(row: list):
    if "_" in row:
        return "row not finished"
    elif "X" in row and not "O" in row:
        return "X"
    elif "O" in row and not "X" in row:
        return "O"
    else:
        return "draw"


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


data = list(input())
grid = create_grid(data)

print("-" * 9)
for row in grid:
    print("|", end="")
    for value in row:
        print(" ", value, sep="", end="")
    print(" |")
print("-" * 9)
print(evaluate_grid(grid))
