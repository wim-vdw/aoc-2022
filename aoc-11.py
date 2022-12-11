from aocd.models import Puzzle
from collections import deque


def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split('\n')]


class Monkey:
    def __init__(self, monkey_id, items: deque, operator, operand, test, throw_true, throw_false):
        self.monkey_id = monkey_id
        self.items = items
        self.operator = operator
        self.operand = operand
        self.test = test
        self.throw_true = int(throw_true)
        self.throw_false = int(throw_false)
        self.inspects = 0

    def add_item(self, item):
        self.items.append(item)

    def increase_inspect(self):
        self.inspects += 1


def part1(puzzle_input):
    """Solve part 1."""
    current_monkey = 0
    monkeys = []
    for line in puzzle_input:
        if line.startswith('Monkey'):
            current_monkey = int(line.split('Monkey')[1].split(':')[0])
        elif 'Starting' in line:
            starting = deque(map(int, line.split(':')[1].split(',')))
        elif 'Operation' in line:
            operator = line.split()[4]
            operand = line.split()[5]
        elif 'Test' in line:
            test = int(line.split()[3])
        elif 'If true' in line:
            throw_true = line.split()[5]
        elif 'If false' in line:
            throw_false = line.split()[5]
            monkeys.append(Monkey(current_monkey, starting, operator, operand, test, throw_true, throw_false))
    for _ in range(20):
        for monkey in monkeys:
            while monkey.items:
                item = monkey.items.popleft()
                monkey.increase_inspect()
                if monkey.operator == '+':
                    if monkey.operand == 'old':
                        item += item
                    else:
                        item += int(monkey.operand)
                else:
                    if monkey.operand == 'old':
                        item *= item
                    else:
                        item *= int(monkey.operand)
                item = item // 3
                if item % monkey.test == 0:
                    monkeys[monkey.throw_true].add_item(item)
                else:
                    monkeys[monkey.throw_false].add_item(item)
    throws = sorted([x.inspects for x in monkeys])
    result = throws[-1] * throws[-2]
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
    puzzle = Puzzle(year=2022, day=11)
    solve(puzzle.input_data)
