import re
from copy import deepcopy


def load(file_name: str) -> list:
    file = open(file_name, 'r')
    lines = file.read()
    lines = lines.split('\n')

    return lines


def command_builder(lines: list) -> list:
    commands = []
    for line in lines:
        matches = re.match(r'([a-z]{3})\s+([+|-]\d+)', line)
        com = {
            "action": matches.group(1),
            "num": int(matches.group(2)),
            "visited": False
        }
        commands.append(com)
    return commands


def part1():
    lines = load('day-08/input.txt')
    commands = command_builder(lines)
    count = 0
    next_command = 0
    while not commands[next_command]['visited']:
        up = 1
        if commands[next_command]['action'] == "acc":
            commands[next_command]['visited'] = True
            count = count + commands[next_command]['num']
        if commands[next_command]['action'] == "jmp":
            commands[next_command]['visited'] = True
            up = commands[next_command]['num']
        if commands[next_command]['action'] == 'nop':
            commands[next_command]['visited'] = True
        next_command += up
    print(count)


def check_it(command_input, change):
    next_command = 0
    count = 0
    while next_command < len(command_input) and not command_input[next_command]['visited'] :
        up = 1
        if next_command == change:
            if command_input[next_command]['action'] == 'jmp':
                command_input[next_command]['action'] = 'nop'
            elif command_input[next_command]['action'] == 'nop':
                command_input[next_command]['action'] = 'jmp'

        if command_input[next_command]['action'] == 'acc':
            command_input[next_command]['visited'] = True
            count = count + command_input[next_command]['num']
        if command_input[next_command]['action'] == 'jmp':
            command_input[next_command]['visited'] = True
            up = command_input[next_command]['num']
        if command_input[next_command]['action'] == 'nop':
            command_input[next_command]['visited'] = True
        next_command += up
    if next_command >= len(command_input):
        return count
    else:
        return 'nope'


def part2():
    lines = load('day-08/input.txt')
    commands_clean = command_builder(lines)

    seen = []
    changable = []
    check = 0
    while check not in seen:
        seen.append(check)
        if commands_clean[check]['action'] == "nop":
            changable.append(check)

        if commands_clean[check]['action'] != "jmp":
            check += 1
        else:
            changable.append(check)
            check += commands_clean[check]['num']

    for change in changable:
        commands = deepcopy(commands_clean)
        value = check_it(commands, change)
        if type(value) == int:
            print(value)


#part1()
part2()
