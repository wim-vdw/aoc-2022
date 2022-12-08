from aocd.models import Puzzle


def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split('\n')]


def part1(puzzle_input):
    """Solve part 1."""
    columns = len(puzzle_input[0])
    rows = len(puzzle_input)
    result = ((columns - 1) * 2) + ((rows - 1) * 2)
    for row in range(1, rows - 1):
        for col in range(1, columns - 1):
            visible = False
            current_tree = puzzle_input[row][col]
            # Check left
            left_ok = True
            for i in range(0, col):
                if puzzle_input[row][i] >= current_tree:
                    left_ok = False
                    break
            if left_ok:
                visible = True
            # Check right
            right_ok = True
            for i in range(col + 1, columns):
                if puzzle_input[row][i] >= current_tree:
                    right_ok = False
                    break
            if right_ok:
                visible = True
            # Check top
            top_ok = True
            for i in range(0, row):
                if puzzle_input[i][col] >= current_tree:
                    top_ok = False
                    break
            if top_ok:
                visible = True
            # Check bottom
            bottom_ok = True
            for i in range(row + 1, rows):
                if puzzle_input[i][col] >= current_tree:
                    bottom_ok = False
                    break
            if bottom_ok:
                visible = True
            if visible:
                result += 1
    print(result)


def part2(puzzle_input):
    """Solve part 2."""
    test = ['30373', '25512', '65332', '33549', '35390']
    puzzle_input = test
    columns = len(puzzle_input[0])
    rows = len(puzzle_input)
    result = ((columns - 1) * 2) + ((rows - 1) * 2)
    for row in range(1, rows - 1):
        for col in range(1, columns - 1):
            visible = False
            current_tree = puzzle_input[row][col]
            # Check left
            left_ok = True
            for i in range(0, col):
                if puzzle_input[row][i] >= current_tree:
                    left_ok = False
                    break
            if left_ok:
                visible = True
            # Check right
            right_ok = True
            for i in range(col + 1, columns):
                if puzzle_input[row][i] >= current_tree:
                    right_ok = False
                    break
            if right_ok:
                visible = True
            # Check top
            top_ok = True
            for i in range(0, row):
                if puzzle_input[i][col] >= current_tree:
                    top_ok = False
                    break
            if top_ok:
                visible = True
            # Check bottom
            bottom_ok = True
            for i in range(row + 1, rows):
                if puzzle_input[i][col] >= current_tree:
                    bottom_ok = False
                    break
            if bottom_ok:
                visible = True
            if visible:
                result += 1
    print(result)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    part1(data)
    part2(data)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=8)
    solve(puzzle.input_data)
