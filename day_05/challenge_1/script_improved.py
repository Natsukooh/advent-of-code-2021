import collections
import re
import sys


def main():
    def parse(line):
        m = re.match(r'(\d+),(\d+) -> (\d+),(\d+)', line)
        return map(int, m.groups())

    def sign(v): return v and (v > 0)*2-1

    C = collections.Counter()
    for a, b, c, d in map(parse, sys.stdin):
        if a == c or b == d:
            dx, dy = sign(c-a), sign(d-b)
            for i in range(max(abs(c-a), abs(d-b)) + 1):
                C[(a + i*dx, b + i*dy)] += 1
    print(sum(C[c] > 1 for c in C))


main()