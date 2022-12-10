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


def crt_draw(crt, cycle, x):
    line = (cycle - 1) // 40
    x_new = (cycle % 40) - 1
    if x_new == -1:
        x_new = 39
    if x_new == x or x_new == x - 1 or x_new == x + 1:
        crt[line][x_new] = '#'


def crt_draw_result(crt):
    for line in crt:
        print(''.join(line))


def part2(puzzle_input):
    """Solve part 2."""
    crt = [['.' for _ in range(40)] for _ in range(6)]
    x_current = 1
    cycle = 0
    for line in puzzle_input:
        if line.startswith('noop'):
            cycle += 1
            crt_draw(crt, cycle, x_current)
        elif line.startswith('addx'):
            _, value = line.split(' ')
            for i in range(1, 2 + 1):
                cycle += 1
                crt_draw(crt, cycle, x_current)
            x_current += int(value)
    crt_draw_result(crt)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    part1(data)
    part2(data)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=10)
    solve(puzzle.input_data)
