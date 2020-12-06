import io
import re

def part1():
    file_name = "input.txt"
    lines = open(file_name, "r").read()
    lines = re.sub(r'\n\n', '!', lines)
    lines = re.sub(r'\n', '', lines)
    lines = re.sub('!',r'\n', lines)
    lines = re.sub(' ', '', lines)
    lines = lines.split('\n')

    count = 0

    for line in lines:
        count += len(set(line))

    print(count)

def part2():
    file_name = "input.txt"
    lines = open(file_name, "r").read()
    groups = lines.split('\n\n')
    
    count = 0

    for group in groups:
        answers = group.split('\n')
        if len(answers) > 1:
            chars = set(answers[0])
            for i in range(1, len(answers)):
                chars = chars & set(answers[i])
            count += len(chars)
        else:
            count += len(answers[0])

    print(count)

part1()
part2()