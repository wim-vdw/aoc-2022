from aocd.models import Puzzle
import heapq


def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split('\n')]


def part1(puzzle_input):
    """Solve part 1."""
    maximum = 0
    current = 0
    for num in puzzle_input:
        if num:
            current += int(num)
        else:
            if current > maximum:
                maximum = current
            current = 0
    if current > maximum:
        maximum = current
    print(maximum)


def part2(puzzle_input):
    """Solve part 2."""
    current = 0
    calories = []
    for num in puzzle_input:
        if num:
            current += int(num)
        else:
            calories.append(current)
            current = 0
    calories.append(current)
    print(sum(heapq.nlargest(3, calories)))


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    part1(data)
    part2(data)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=1)
    solve(puzzle.input_data)
