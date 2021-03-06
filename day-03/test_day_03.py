from day_03 import tree_finder

def test_tree_finder_finds_a_tree():
    map_data = [".#..#","...#."]
    down = 1
    right = 3
    
    result = tree_finder(
        map_data=map_data,
        down=down,
        right=right
    )

    assert result == 1


def test_tree_finder_not_find_tree():
    map_data = [".#..#","....."]
    down = 1
    right = 3
    
    result = tree_finder(
        map_data=map_data,
        down=down,
        right=right
    )

    assert result == 0


def test_tree_finder_handles_wrap_around():
    map_data = [
        "..##.........##.........##.........##.........##.........##.......",
        "#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..",
        ".#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.",
        "..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#",
        ".#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.",
        "..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....",
        ".#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#",
        ".#........#.#........#.#........#.#........#.#........#.#........#",
        "#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...",
        "#...##....##...##....##...##....##...##....##...##....##...##....#",
        ".#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#"
    ]
    down = 1
    right = 3
    
    result = tree_finder(
        map_data=map_data,
        down=down,
        right=right
    )

    assert result == 7