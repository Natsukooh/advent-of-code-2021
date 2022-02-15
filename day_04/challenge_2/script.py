import sys


def main():
    numbers = [int(num) for num in sys.stdin.readline().split(",")]
    sys.stdin.readline()
    grids = [[[int(num) for num in trim(sys.stdin.readline()).split(" ")] for _ in range(5)]]
    while sys.stdin.readline() == "\n":
        grids.append([[int(num) for num in trim(sys.stdin.readline()).split(" ")] for _ in range(5)])

    i = 0
    win = []
    while len(grids) > 1:
        delete_number(numbers[i], grids)
        i += 1
        win = check_win(grids)
        win.sort(reverse=True)
        for id in win:
            grids.pop(id)

    while not check_win(grids):
        delete_number(numbers[i], grids)
        i += 1

    score = calculate_score(grids[0], numbers[i-1])
    print(score)


def check_win(grids):
    winners = []
    for i, grid in enumerate(grids):
        if win_length(grid) or win_width(grid) or win_diagonals(grid):
            winners.append(i)
    return winners


def delete_number(n, grids):
    for grid in grids:
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                grid[i][j] = -1 * (grid[i][j] + 1) if grid[i][j] == n else grid[i][j]


def win_length(grid):
    for i in range(len(grid)):
        winning = True
        for j in range(len(grid[i])):
            if grid[i][j] >= 0:
                winning = False
                break
        if winning:
            return True
    return False


def win_width(grid):
    for j in range(len(grid[0])):
        winning = True
        for i in range(len(grid)):
            if grid[i][j] >= 0:
                winning = False
                break
        if winning:
            return True
    return False


def win_diagonals(grid):
    for i in range(len(grid)):
        winning = True
        if grid[i][i] >= 0:
            winning = False
            break
    if winning:
        return True

    for i in range(len(grid)):
        winning = True
        if grid[len(grid) - i - 1][len(grid) - i - 1] >= 0:
            winning = False
            break
    if winning:
        return True

    return False


def calculate_score(grid, n):
    sum = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            sum += grid[i][j] if grid[i][j] >= 0 else 0
    return sum * n


def trim(str):
    prev_is_space = True
    new_str = ""
    for char in str:
        if char != " " or not prev_is_space:
            new_str += char
        prev_is_space = True if char == " " else False
    return new_str


main()
