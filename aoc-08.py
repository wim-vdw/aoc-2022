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
            current_tree = puzzle_input[row][col]
            # Check left
            left_ok = True
            for i in range(0, col):
                if puzzle_input[row][i] >= current_tree:
                    left_ok = False
                    break
            # Check right
            right_ok = True
            for i in range(col + 1, columns):
                if puzzle_input[row][i] >= current_tree:
                    right_ok = False
                    break
            # Check top
            top_ok = True
            for i in range(0, row):
                if puzzle_input[i][col] >= current_tree:
                    top_ok = False
                    break
            # Check bottom
            bottom_ok = True
            for i in range(row + 1, rows):
                if puzzle_input[i][col] >= current_tree:
                    bottom_ok = False
                    break
            if any([left_ok, right_ok, top_ok, bottom_ok]):
                result += 1
    print(result)


def part2(puzzle_input):
    """Solve part 2."""
    columns = len(puzzle_input[0])
    rows = len(puzzle_input)
    result = 0
    for row in range(1, rows - 1):
        for col in range(1, columns - 1):
            current_tree = puzzle_input[row][col]
            left, right, top, bottom = 0, 0, 0, 0
            # Check left
            for i in range(col - 1, -1, -1):
                left += 1
                if puzzle_input[row][i] >= current_tree:
                    break
            # Check right
            for i in range(col + 1, columns):
                right += 1
                if puzzle_input[row][i] >= current_tree:
                    break
            # Check top
            for i in range(row - 1, -1, -1):
                top += 1
                if puzzle_input[i][col] >= current_tree:
                    break
            # Check bottom
            for i in range(row + 1, rows):
                bottom += 1
                if puzzle_input[i][col] >= current_tree:
                    break
            scenic_score = left * right * top * bottom
            if scenic_score > result:
                result = scenic_score
    print(result)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    part1(data)
    part2(data)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=8)
    solve(puzzle.input_data)
