import sys


def main():
    total = 0
    for line in sys.stdin:
        content = line.split("|")[1].split()
        for number in content:
            if 2 <= len(number) <= 4 or len(number) == 7:
                total += 1
    print(total)


main()
