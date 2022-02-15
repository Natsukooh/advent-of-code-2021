import collections
import sys


def main():
    C = collections.Counter()
    numbers = list(map(int, sys.stdin.readline().split(",")))
    max_number = max(numbers)
    for number in numbers:
        for i in range(0, max_number+1):
            C[i] += int((abs(number - i) * (abs(number - i) + 1)) / 2)

    print(min(C.values()))


main()