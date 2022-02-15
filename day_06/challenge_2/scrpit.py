import sys
import collections


def main():
    numbers = list(map(int, sys.stdin.readline().split(",")))
    days = 0
    C = [0 for _ in range(max(numbers)+10)]
    for number in numbers:
        C[number] += 1

    while days < 256:
        C.append(0)
        if C[days] != 0:
            C[days + 7] += C[days]
            C[days + 9] += C[days]
            C[days] = 0
        days += 1

    sum = 0
    for number in C:
        sum += number

    print(sum)


main()