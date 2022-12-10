from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split('\n')]


def tail_needs_to_move(head_x, head_y, tail_x, tail_y):
    x_diff = head_x - tail_x
    y_diff = head_y - tail_y
    return abs(x_diff) > 1 or abs(y_diff) > 1


def part1(puzzle_input):
    """Solve part 1."""
    head_x, head_y, tail_x, tail_y = 0, 0, 0, 0
    tail_locations = set()
    for motion in puzzle_input:
        direction, steps = motion.split()
        for step in range(int(steps)):
            if direction == 'R':
                head_x += 1
            if direction == 'L':
                head_x -= 1
            if direction == 'U':
                head_y += 1
            if direction == 'D':
                head_y -= 1
            if tail_needs_to_move(head_x, head_y, tail_x, tail_y):
                if direction == 'R':
                    tail_y = head_y
                    tail_x = head_x - 1
                if direction == 'L':
                    tail_y = head_y
                    tail_x = head_x + 1
                if direction == 'U':
                    tail_x = head_x
                    tail_y = head_y - 1
                if direction == 'D':
                    tail_x = head_x
                    tail_y = head_y + 1
                tail_location = f'{tail_x}:{tail_y}'
                tail_locations.add(tail_location)
    result = len(tail_locations) + 1
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
    puzzle = Puzzle(year=2022, day=9)
    solve(puzzle.input_data)
