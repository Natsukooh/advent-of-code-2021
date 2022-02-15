def main():
    file = open("../input", "r")

    horizontal_position = 0
    depth = 0

    while True:
        line = file.readline()

        if not line:
            break

        instruction = line.split()[0]
        amount = int(line.split()[1])

        if instruction == "forward":
            horizontal_position += amount

        elif instruction == "down":
            depth += amount

        else:
            depth -= amount

    print(f"horizontal position = {horizontal_position}, depth = {depth}, answer is {horizontal_position * depth}")


main()