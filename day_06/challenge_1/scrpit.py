import sys


def main():
    numbers = list(map(int, sys.stdin.readline().split(",")))
    days = 0
    to_append = []
    while days != 256:
        print(days, end=" ")
        for i in range(len(numbers)):
            numbers[i] -= 1
            if numbers[i] == -1:
                numbers[i] = 6
                to_append.append(8)
        numbers += to_append
        to_append = []
        days += 1

    print(len(numbers))


main()