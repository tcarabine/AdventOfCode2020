from copy import deepcopy


def load(file_name: str) -> list:
    file = open(file_name, 'r')
    lines = file.read()
    lines = lines.split('\n')
    ret_lines = []
    for line in lines:
        ret_lines.append(list(line))
    return ret_lines


def get_occupancy(seat_plan: list, pos: tuple) -> chr:
    to_check = []
    for i in [-1, 0, 1]:
        for j in [-1, 0, 1]:
            x = pos[1] + j
            y = pos[0] + i
            if (x >= 0 and y >= 0 and x < len(seat_plan[pos[0]]) and y < len(seat_plan) and (y, x) != pos):
                to_check.append((y, x))
    adj_occ_count = 0
    for adj_pos in to_check:
        if seat_plan[adj_pos[0]][adj_pos[1]] == '#':
            adj_occ_count += 1
    if (
        adj_occ_count < 4 and seat_plan[pos[0]][pos[1]] == '#'
        ) or (
            adj_occ_count == 0 and seat_plan[pos[0]][pos[1]] == 'L'
            ):
        return '#'
    else:
        return 'L'


def part1():
    current_state = load('day-11/input.txt')
    floor = '.'
    itterations = 0
    changed = True
    while changed:
        new_state = deepcopy(current_state)
        for row_num in range(len(current_state)):
            for seat_num in range(len(current_state[row_num])):
                space = current_state[row_num][seat_num]
                space_result = ''
                if space == floor:
                    space_result = floor
                else:
                    space_result = get_occupancy(
                        current_state, (row_num, seat_num)
                    )

                new_state[row_num][seat_num] = space_result
        row_changed = []
        for row in range(len(current_state)):
            if str(current_state[row]) == str(new_state[row]):
                row_changed.append(False)
            else:
                row_changed.append(True)
        changed = True if True in row_changed else False
        itterations += 1
        print(f"{itterations}")
        current_state = deepcopy(new_state)
    occupied = 0
    for row in current_state:
        occupied += row.count('#')
    print(occupied)


def get_occupancy_v2(seat_plan: list, pos: tuple) -> chr:
    adj_occ_count = 0
    # check Up
    for y in range(pos[0], -1, -1):
        x = pos[1]
        if (y, x) != pos and seat_plan[y][x] != '.':
            if seat_plan[y][x] == '#':
                adj_occ_count += 1
            break
    # check Down
    for y in range(pos[0], len(seat_plan), 1):
        x = pos[1]
        if (y, x) != pos and seat_plan[y][x] != '.':
            if seat_plan[y][x] == '#':
                adj_occ_count += 1
            break
    # check Left
    for x in range(pos[1], -1, -1):
        y = pos[0]
        if (y, x) != pos and seat_plan[y][x] != '.':
            if seat_plan[y][x] == '#':
                adj_occ_count += 1
            break
    # check Right
    for x in range(pos[1], len(seat_plan[pos[0]]), 1):
        y = pos[0]
        if (y, x) != pos and seat_plan[y][x] != '.':
            if seat_plan[y][x] == '#':
                adj_occ_count += 1
            break

    # check up left
    y = pos[0]
    x = pos[1]
    while x >= 0 and y >= 0:
        if (y, x) != pos and seat_plan[y][x] != '.':
            if seat_plan[y][x] == '#':
                adj_occ_count += 1
            break
        x += -1
        y += -1

    # check up right
    y = pos[0]
    x = pos[1]
    while x < len(seat_plan[0]) and y >= 0:
        if (y, x) != pos and seat_plan[y][x] != '.':
            if seat_plan[y][x] == '#':
                adj_occ_count += 1
            break
        x += 1
        y += -1

    # check down left
    y = pos[0]
    x = pos[1]
    while x >= 0 and y < len(seat_plan):
        if (y, x) != pos and seat_plan[y][x] != '.':
            if seat_plan[y][x] == '#':
                adj_occ_count += 1
            break
        x += -1
        y += 1

    # check down right
    y = pos[0]
    x = pos[1]
    while x < len(seat_plan[0]) and y < len(seat_plan):
        if (y, x) != pos and seat_plan[y][x] != '.':
            if seat_plan[y][x] == '#':
                adj_occ_count += 1
            break
        x += 1
        y += 1

    if seat_plan[pos[0]][pos[1]] == '#' and adj_occ_count >= 5:
        return 'L'
    elif seat_plan[pos[0]][pos[1]] == '#' and adj_occ_count <5:
        return '#'
    elif seat_plan[pos[0]][pos[1]] == 'L' and adj_occ_count == 0:
        return '#'
    else:
        return seat_plan[pos[0]][pos[1]]


def part2():
    current_state = load('day-11/input.txt')
    floor = '.'
    itterations = 0
    changed = True
    while changed:
        new_state = deepcopy(current_state)
        for row_num in range(len(current_state)):
            for seat_num in range(len(current_state[row_num])):
                space = current_state[row_num][seat_num]
                space_result = ''
                if space == floor:
                    space_result = floor
                else:
                    space_result = get_occupancy_v2(
                        current_state, (row_num, seat_num)
                    )
                new_state[row_num][seat_num] = space_result
        row_changed = []
        for row in range(len(current_state)):
            if str(current_state[row]) == str(new_state[row]):
                row_changed.append(False)
            else:
                row_changed.append(True)
        changed = True if True in row_changed else False
        itterations += 1
        current_state = deepcopy(new_state)
    occupied = 0
    for row in current_state:
        occupied += row.count('#')
    print(occupied)


part1()
part2()
