def load(file_name: str) -> list:
    file = open(file_name, 'r')
    lines = file.read()
    lines = lines.split('\n')
    return lines


def turn(facing: chr, deg: int) -> chr:
    compass = {
        'N': 0,
        'E': 90,
        'S': 180,
        'W': 270
    }

    new_dir = (compass[facing] + deg) % 360
    return list(compass.keys())[list(compass.values()).index(new_dir)]


def move(direction: chr, pos: tuple, facing: chr, value: int) -> tuple:
    if direction == 'F':
        direction = facing
    if direction == 'N':
        return (pos[0], pos[1] + value)
    elif direction == 'E':
        return (pos[0] + value, pos[1])
    elif direction == 'S':
        return (pos[0], pos[1] - value)
    elif direction == 'W':
        return (pos[0] - value, pos[1])


def turn_waypoint(waypoint: tuple, deg: int) -> tuple:
    turn = (360 + deg) % 360
    if turn == 0:
        return waypoint
    elif turn == 90:
        return ( waypoint[1], -1 * waypoint[0])
    elif turn == 180:
        return ( -1 * waypoint[0], -1 * waypoint[1])
    elif turn == 270:
        return (-1* waypoint[1], waypoint[0])
    

def move_to_waypoint(pos: tuple, waypoint: tuple, times: int) -> tuple:
    for i in range(times):
        pos = (pos[0] + waypoint[0], pos[1] + waypoint[1])
    return pos


def manhattan(position: tuple) -> int:
    return abs(position[0]) + abs(position[1])


def part1():
    file_name = 'day-12/input.txt'
    instructions = load(file_name)
    facing = 'E'
    pos = (0, 0)
    print(f"{facing} - {pos}")
    for instruction in instructions:
        if instruction[0] in ['L', 'R']:
            deg = int(instruction[1:]) if instruction[0] == 'R' else -1 * int(instruction[1:])
            facing = turn(facing, deg)
        else:
            pos = move(instruction[0], pos, facing, int(instruction[1:]))
        print(f"{facing} - {pos}") 
    print(manhattan(pos))


def part2():
    file_name = 'day-12/input.txt'
    instructions = load(file_name)
    pos = (0, 0)
    waypoint = (10, 1)
    print(f"{pos} - {waypoint}")
    for instruction in instructions:
        print(instruction)
        if instruction[0] in ['L', 'R']:
            deg = int(instruction[1:]) if instruction[0] == 'R' else -1 * int(instruction[1:])
            waypoint = turn_waypoint(waypoint, deg)
        elif instruction[0] == 'F':
            pos = move_to_waypoint(pos, waypoint, int(instruction[1:]))
        else:
            waypoint = move(instruction[0], waypoint, '', int(instruction[1:]))
        print(f"{pos} - {waypoint}") 
    print(manhattan(pos))


part1()
part2()
