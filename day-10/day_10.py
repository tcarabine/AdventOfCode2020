from collections import defaultdict


def load(file_name: str) -> list:
    file = open(file_name, 'r')
    lines = file.read()
    lines = lines.split('\n')
    lines = [int(x) for x in lines]
    return lines


def part1():
    lines = load('day-10/input.txt')
    # Add first and last
    lines.append(0)
    lines.sort()
    lines.append(lines[-1] + 3)
    diff_one = 0
    diff_two = 0
    diff_three = 0

    for i in range(1, len(lines)):
        diff = lines[i] - lines[i - 1]
        if diff == 1:
            diff_one += 1
        elif diff == 2:
            diff_two += 1
        elif diff == 3:
            diff_three += 1
        else:
            print('This looks bad')
    print(f"1 - {diff_one}\t2 - {diff_two}\t3 - {diff_three}")
    print(diff_one * diff_three)


def part2():
    lines = load('day-10/input.txt')
    # Add first and last
    lines.append(0)
    lines.sort()
    lines.append(lines[-1] + 3)

    combos = defaultdict(int)
    combos[0] = 1

    for plug in lines:
        for step in range(1, 4):
            possible = plug + step
            if possible in lines:
                # Combo to possible is all combos to a valid previous step summed
                combos[possible] += combos[plug]

    print(combos[lines[-1]])


part1()
part2()
