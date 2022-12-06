from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split('\n')][0]


def part1(puzzle_input):
    """Solve part 1."""
    for i in range(3, len(puzzle_input)):
        tmp = set(puzzle_input[i - 3:i + 1])
        if len(tmp) == 4:
            print(i + 1)
            break


def part2(puzzle_input):
    """Solve part 2."""
    for i in range(13, len(puzzle_input)):
        tmp = set(puzzle_input[i - 13:i + 1])
        if len(tmp) == 14:
            print(i + 1)
            break


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    part1(data)
    part2(data)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=6)
    solve(puzzle.input_data)
