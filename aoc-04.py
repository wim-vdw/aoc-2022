from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split('\n')]


def part1(puzzle_input):
    """Solve part 1."""
    result = 0
    for sections in puzzle_input:
        sections1, sections2 = sections.split(',')
        sections1_start, sections1_end = map(int, sections1.split('-'))
        sections2_start, sections2_end = map(int, sections2.split('-'))
        if (sections1_start <= sections2_start and sections1_end >= sections2_end) or \
                (sections2_start <= sections1_start and sections2_end >= sections1_end):
            result += 1
    print(result)


def part2(puzzle_input):
    """Solve part 2."""
    result = 0
    for sections in puzzle_input:
        sections1, sections2 = sections.split(',')
        sections1_start, sections1_end = map(int, sections1.split('-'))
        sections2_start, sections2_end = map(int, sections2.split('-'))
        sections1_set = set([x for x in range(sections1_start, sections1_end + 1)])
        sections2_set = set([x for x in range(sections2_start, sections2_end + 1)])
        if sections1_set & sections2_set:
            result += 1
    print(result)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    part1(data)
    part2(data)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=4)
    solve(puzzle.input_data)
