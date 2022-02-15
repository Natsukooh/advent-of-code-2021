import sys


def main():
    score = 0
    scores =\
    {
        ")": 3,
        "]": 57,
        "}": 1197,
        ">": 25137
    }
    matches =\
    {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }

    for line in sys.stdin:
        pile = []
        for char in line:
            if char != "\n":
                if char in ["<", "(", "{", "["]:
                    pile.append(char)
                else:
                    popped = pile.pop(len(pile)-1)
                    if matches[popped] != char:
                        score += scores[char]
                        break
    print(score)


main()