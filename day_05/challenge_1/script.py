import sys


def main():
    grid = [["." for _ in range(1000)] for _ in range(1000)]
    while True:
        line = sys.stdin.readline().split(",")
        if line == [""]:
            break

        x1 = int(line[0])
        y1 = int(line[1].split()[0])
        x2 = int(line[1].split()[2])
        y2 = int(line[2])

        if x1 == x2:
            _range = range(y1, y2+1) if y1 < y2 else range(y2, y1+1)
            for y in _range:
                grid[y][x1] = 1 if grid[y][x1] == "." else grid[y][x1] + 1
        elif y1 == y2:
            _range = range(x1, x2+1) if x1 < x2 else range(x2, x1+1)
            for x in _range:
                grid[y1][x] = 1 if grid[y1][x] == "." else grid[y1][x] + 1

    count = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] != "." and grid[x][y] >= 2:
                count += 1

    print(count)


def print_grid(grid):
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            print(grid[x][y], end=" ")
        print()

main()