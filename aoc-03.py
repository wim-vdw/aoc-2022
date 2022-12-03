from aocd.models import Puzzle
from string import ascii_lowercase, ascii_uppercase

values_lowercase = dict(zip(ascii_lowercase, [x for x in range(1, 26 + 1)]))
values_uppercase = dict(zip(ascii_uppercase, [x for x in range(27, 52 + 1)]))
values_all = values_lowercase | values_uppercase


def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split('\n')]


def part1(puzzle_input):
    """Solve part 1."""
    result = 0
    for rucksack in puzzle_input:
        compartment1 = set(rucksack[:len(rucksack) // 2])
        compartment2 = set(rucksack[len(rucksack) // 2:])
        common_item = (compartment1 & compartment2).pop()
        result += values_all[common_item]
    print(result)


def part2(puzzle_input):
    """Solve part 2."""
    group = []
    result = 0
    for rucksack in puzzle_input:
        group.append(rucksack)
        if len(group) == 3:
            elve1, elve2, elve3 = set(group[0]), set(group[1]), set(group[2])
            common_item = (elve1 & elve2 & elve3)
            result += values_all[common_item.pop()]
            group.clear()
    print(result)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    part1(data)
    part2(data)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=3)
    solve(puzzle.input_data)
