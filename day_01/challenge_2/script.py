def main():
    file = open("../input", "r")
    line_no = 0
    sums = []

    while True:
        line = file.readline()

        if not line:
            break

        depth = int(line)

        sums.append(depth)

        if line_no-1 >= 0:
            sums[line_no-1] += depth

        if line_no-2 >= 0:
            sums[line_no-2] += depth

        line_no += 1

    previous = sums[0]
    measurement_larger_than_previous = 0
    i = 1

    while(i < len(sums) - 2):
        if sums[i] > previous:
            measurement_larger_than_previous += 1
        previous = sums[i]
        i+=1

    print(measurement_larger_than_previous)


main()