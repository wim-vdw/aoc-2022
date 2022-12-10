from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split('\n')]


def calculate(cycle, x):
    if cycle == 20:
        return 20 * x
    elif cycle == 60:
        return 60 * x
    elif cycle == 100:
        return 100 * x
    elif cycle == 140:
        return 140 * x
    elif cycle == 180:
        return 180 * x
    elif cycle == 220:
        return 220 * x
    return 0


def part1(puzzle_input):
    """Solve part 1."""
    x = 1
    cycle = 0
    result = 0
    for line in puzzle_input:
        if line.startswith('noop'):
            cycle += 1
            result += calculate(cycle, x)
        elif line.startswith('addx'):
            _, value = line.split(' ')
            for i in range(1, 2 + 1):
                cycle += 1
                result += calculate(cycle, x)
            x += int(value)
    print(result)


def part2(puzzle_input):
    """Solve part 2."""
    pass


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    part1(data)
    part2(data)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=10)
    solve(puzzle.input_data)
