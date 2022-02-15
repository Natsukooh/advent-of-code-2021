import sys


def main():
    grid = []
    for i, line in enumerate(sys.stdin):
        grid.append([])
        for char in line:
            if char != "\n":
                char = int(char)
                grid[i].append(char)

    total = 0
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            to_pick = True
            if x-1 >= 0:
                if grid[x-1][y] <= grid[x][y]:
                    to_pick = False
            if to_pick:
                if y-1 >= 0:
                    if grid[x][y - 1] <= grid[x][y]:
                        to_pick = False
            if to_pick:
                if y+1 < len(grid[x]):
                    if grid[x][y + 1] <= grid[x][y]:
                        to_pick = False
            if to_pick:
                if x+1 < len(grid):
                    if grid[x + 1][y] <= grid[x][y]:
                        to_pick = False
            if to_pick:
                total += grid[x][y] + 1

    print(total)


main()