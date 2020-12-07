def part1():
    file_name = "input.txt"
    lines = open(file_name, "r").readlines()
    seats = []

    for line in lines:
        line = line.replace("B", "1").replace("F", "0")
        line = line.replace("R", "1").replace("L", "0")
        seats.append(int(line, 2))

    seats.sort()
    print(seats[-1])


def part2():
    file_name = "input.txt"
    lines = open(file_name, "r").readlines()
    seats = []

    for line in lines:
        line = line.replace("B", "1").replace("F", "0")
        line = line.replace("R", "1").replace("L", "0")
        seats.append(int(line, 2))

    seats.sort()

    for i in range(len(seats) - 1):
        if seats[i+1] - seats[i] == 2:
            print(seats[i] + 1)


part1()
part2()
