import sys


def main():
    grid = []
    for line in sys.stdin:
        grid.append([int(char) if char != "\n" else None for char in line])
    for x in range(len(grid)):
        for y in range(len(grid[x])):
            if grid[x][y] is None:
                grid[x].pop(y)

    flashes = 0
    for generation in range(100):
        to_flash = []
        for x in range(len(grid)):
            for y in range(len(grid[x])):
                grid[x][y] += 1
                if grid[x][y] > 9:
                    to_flash.append((x, y))

        while len(to_flash) != 0:
            x, y = to_flash.pop(len(to_flash) - 1)
            flashes_to_add = flash(grid, x, y)
            flashes += flashes_to_add

    print(flashes)


def flash(grid, x, y):
    flashes = 0
    if grid[x][y] != 0:
        grid[x][y] = 0
        flashes += 1
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[x + dx]):
                    if grid[x + dx][y + dy] != 0:
                        grid[x + dx][y + dy] += 1
                        if grid[x + dx][y + dy] > 9:
                            flashes += flash(grid, x + dx, y + dy)
    return flashes


main()
