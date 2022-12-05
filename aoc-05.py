from aocd.models import Puzzle
from collections import defaultdict, deque


def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split('\n')]


def part1(puzzle_input):
    """Solve part 1."""
    stacks = defaultdict(deque)
    for line in puzzle_input:
        if '[' in line:
            number_of_stacks = (len(line) + 1) // 4
            for i in range(number_of_stacks):
                crate = line[i * 4 + 1]
                if crate != ' ':
                    stacks[i + 1].append(crate)
        if 'move' in line:
            data = line.split(' ')
            quantity = int(data[1])
            source = int(data[3])
            target = int(data[5])
            for _ in range(quantity):
                stacks[target].appendleft(stacks[source].popleft())
    result = ''
    for i in range(1, len(stacks) + 1):
        result += stacks[i].popleft()
    print(result)


def part2(puzzle_input):
    """Solve part 2."""
    stacks = defaultdict(deque)
    for line in puzzle_input:
        if '[' in line:
            number_of_stacks = (len(line) + 1) // 4
            for i in range(number_of_stacks):
                crate = line[i * 4 + 1]
                if crate != ' ':
                    stacks[i + 1].append(crate)
        if 'move' in line:
            data = line.split(' ')
            quantity = int(data[1])
            source = int(data[3])
            target = int(data[5])
            tmp = deque()
            for _ in range(quantity):
                tmp.append(stacks[source].popleft())
            while tmp:
                stacks[target].appendleft(tmp.pop())
    result = ''
    for i in range(1, len(stacks) + 1):
        result += stacks[i].popleft()
    print(result)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    part1(data)
    part2(data)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=5)
    solve(puzzle.input_data)
