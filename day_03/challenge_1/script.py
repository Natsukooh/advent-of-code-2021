import sys


def main():
    lines = [line for line in sys.stdin]
    lines_bis = [line for line in lines]
    length = len(lines[0])

    i = 0

    while len(lines) > 1:
        zeros = 0
        ones = 0

        for line in lines:
            if line[i] == "0":
                zeros += 1
            else:
                ones += 1

        if zeros > ones:
            lines = list(filter(lambda line: line[i] == "0", lines))
        else:
            lines = list(filter(lambda line: line[i] == "1", lines))

        i += 1

    i = 0

    while len(lines_bis) > 1:
        zeros = 0
        ones = 0

        for line in lines_bis:
            if line[i] == "0":
                zeros += 1
            else:
                ones += 1

        if zeros > ones:
            lines_bis = list(filter(lambda line: line[i] == "1", lines_bis))
        else:
            lines_bis = list(filter(lambda line: line[i] == "0", lines_bis))

        i += 1

    print(int(lines[0], 2) * int(lines_bis[0], 2))


main()