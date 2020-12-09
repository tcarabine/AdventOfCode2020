def build_preamble(previous: list) -> set:
    preamble = set()
    for i in previous:
        for j in previous:
            if i != j:
                preamble.add(i+j)
    return preamble


def load(file_name: str) -> list:
    file = open(file_name, 'r')
    lines = file.read()
    lines = lines.split('\n')

    return lines


def find_first_weakness(preamble_length: int, numbers: list) -> tuple:
    preamble = build_preamble(numbers[:preamble_length])
    discard = []
    found_first = False
    while not found_first and len(numbers) > 0:
        if numbers[preamble_length] not in preamble:
            found_first = True
            return(numbers[preamble_length],discard)
        else:
            discard.append(numbers[0])
            numbers.remove(numbers[0])
            preamble = build_preamble(numbers[:preamble_length])


def find_range(target: int, numbers: list) -> list:
    for start in range(len(numbers)):
        count = 0
        for pos in range(start, len(numbers)):
            count += numbers[pos]
            if count == target:
                return numbers[start:pos]


def part1():
    numbers = [int(n) for n in load('day-09/input.txt')]
    print(find_first_weakness(25, numbers)[0])


def part2():
    numbers_1 = [int(n) for n in load('day-09/input.txt')]
    weakness = find_first_weakness(25, numbers_1)
    weak_range = find_range(weakness[0], weakness[1])
    weak_range.sort()
    print(weak_range[0] + weak_range[-1])


part1()
part2()
