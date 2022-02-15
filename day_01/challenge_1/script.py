def main():
    file = open("../input", "r")
    measurement_larger_than_previous = 0
    previous = -1

    while True:
        line = file.readline()

        if not line:
            break

        depth = int(line)
        if previous != -1 and previous < depth:
            measurement_larger_than_previous += 1

        previous = depth

    print(measurement_larger_than_previous)

main()