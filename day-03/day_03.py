import io
from functools import reduce

def tree_finder(map_data: list, right: int, down: int, tree_char: chr = '#') -> int:
    height = len(map_data)
    width = len(map_data[0])
    x = 0
    y = 0
    trees = 0

    while (y+down < height):
        x += right
        y += down

        pos_x = x % width
        
        # Check for trees
        if map_data[y][pos_x] == tree_char:
            # map_data[y] = f"{map_data[y][:pos_x]}X{map_data[y][pos_x + 1:]}"
            trees += 1
        # else:
            # map_data[y]= f"{map_data[y][:pos_x]}O{map_data[y][pos_x + 1:]}"
    
    for line in map_data:
        print(line)
    return trees

def part1():
    file_name = "input.txt"

    file = open(file_name, "r")
    lines = file.read().splitlines() 


    trees_hit = tree_finder(
        map_data=lines,
        right=3,
        down=1
    )

    print(trees_hit)

def part2():
    file_name = "input.txt"

    file = open(file_name, "r")
    lines = file.read().splitlines() 

    attempts = [
        [1,1],
        [3,1],
        [5,1],
        [7,1],
        [1,2]
    ]

    trees = []

    for attempt in attempts:
        trees.append(tree_finder(
            map_data=lines,
            right=attempt[0],
            down=attempt[1]
        ))

    print(trees)
    result = reduce((lambda a,b: a*b), trees)
    print(result)

part1()
part2()