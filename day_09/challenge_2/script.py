import sys


def main():
    grid = []
    for i, line in enumerate(sys.stdin):
        grid.append([])
        for char in line:
            if char != "\n":
                char = int(char)
                grid[i].append(char)

    sizes = []
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] != "+" and grid[x][y] != 9:
                size = spread(grid, x, y)
                print(f"spreading from ({x},{y}) : {size} + spread")
                sizes.append(size)

    sizes.sort(reverse=True)
    print(sizes[0] * sizes[1] * sizes[2])


def spread(grid, x, y):
    total = 0
    if x - 1 >= 0:
        if grid[x - 1][y] != 9 and grid[x - 1][y] != "+":
            grid[x - 1][y] = "+"
            total += 1
            total += spread(grid, x - 1, y)
    if y - 1 >= 0:
        if grid[x][y - 1] != 9 and grid[x][y - 1] != "+":
            grid[x][y - 1] = "+"
            total += 1
            total += spread(grid, x, y - 1)
    if y + 1 < len(grid[x]):
        if grid[x][y + 1] != 9 and grid[x][y + 1] != "+":
            grid[x][y + 1] = "+"
            total += 1
            total += spread(grid, x, y + 1)
    if x + 1 < len(grid):
        if grid[x + 1][y] != 9 and grid[x + 1][y] != "+":
            grid[x + 1][y] = "+"
            total += 1
            total += spread(grid, x + 1, y)
    return total


main()