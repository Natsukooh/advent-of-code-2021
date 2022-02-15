import sys


def main():
    scores = []
    points =\
    {
        "(": 1,
        "[": 2,
        "{": 3,
        "<": 4
    }
    matches =\
    {
        "(": ")",
        "[": "]",
        "{": "}",
        "<": ">"
    }

    for line in sys.stdin:
        score = 0
        good = True
        pile = []

        for char in line:
            if char != "\n":
                if char in ["<", "(", "{", "["]:
                    pile.append(char)
                else:
                    popped = pile.pop(len(pile) - 1)
                    if matches[popped] != char:
                        good = False
                        break

        if good:
            while len(pile) > 0:
                char = pile.pop(len(pile)-1)
                score = score * 5 + points[char]

            scores.append(score)

    scores.sort()
    print(scores[int((len(scores) - 1)/2)])


main()