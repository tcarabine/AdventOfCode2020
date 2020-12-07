import re
from collections import defaultdict


def load(file_name: str) -> list:
    file = open(file_name, 'r')
    lines = file.read()
    lines = lines.split('\n')

    return lines


def searcher(search: str, rule_dict: defaultdict) -> defaultdict:
    outer = rule_dict[search]
    if len(outer) == 0:
        return outer
    return outer.union(
        colour2 for colour in outer for colour2 in searcher(colour, rule_dict)
    )


def rule_parser_part2(rules: str):
    rules = rules.split(' contain ')
    colour = re.sub(r'(.*)\s(bags|bag)', r'\g<1>', rules[0])
    children = []
    if rules[1] != 'no other bags.':
        for rule in rules[1].split(','):
            match = re.match(
                r'.*(\d+)\s(.*)\s(bags\.|bags|bag\.|bag)',
                rule
            )
            # match 2 => inside bag colour
            # match 1 => how many it holds
            children.append((match.group(2), int(match.group(1))))
    return (colour, children)


def must_have(this_bag: str, contents: dict):
    return sum(holds + holds * must_have(colour, contents) for colour, holds in contents[this_bag])


def part1(my_bag: str):
    lines = load('day-07/input.txt')

    rule_dict = defaultdict(set)
    for rules in lines:
        rules = rules.split(' contain ')
        key = re.sub(r'(.*)\s(bags|bag)', r'\g<1>', rules[0])
        if rules[1] != 'no other bags.':
            for rule in rules[1].split(','):
                match = re.match(
                    r'.*(\d+)\s(.*)\s(bags\.|bags|bag\.|bag)',
                    rule
                )
                rule_dict[match.group(2)].add(key)
    count = len(searcher(my_bag, rule_dict))
    print(count)


def part2(my_bag: str):
    lines = load('day-07/input.txt')
    contents = dict(rule_parser_part2(rules) for rules in lines)

    count = must_have(my_bag, contents)
    print(count)


my_bag = "shiny gold"
part1(my_bag)
part2(my_bag)
