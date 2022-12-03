from aocd.models import Puzzle

SHAPE = {
    'X': 1,  # Rock
    'Y': 2,  # Paper
    'Z': 3,  # Scissors
}

DRAW = ['A X', 'B Y', 'C Z']
WIN = ['C X', 'A Y', 'B Z']
LOSS = ['A Z', 'B X', 'C Y']


def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split('\n')]


def part1(puzzle_input):
    """Solve part 1."""
    total_score = 0
    for current_round in puzzle_input:
        player1, player2 = current_round.split()
        current_score = SHAPE[player2]
        if current_round in DRAW:
            current_score += 3
        elif current_round in WIN:
            current_score += 6
        elif current_round in LOSS:
            pass
        total_score += current_score
    print(total_score)


def part2(puzzle_input):
    """Solve part 2."""
    total_score = 0
    for current_round in puzzle_input:
        player1, how_to_end = current_round.split()
        if how_to_end == 'X':
            for lose in LOSS:
                if lose[0] == player1:
                    total_score += SHAPE[lose[2]]
                    break
        if how_to_end == 'Y':
            total_score += 3
            for draw in DRAW:
                if draw[0] == player1:
                    total_score += SHAPE[draw[2]]
                    break
        if how_to_end == 'Z':
            total_score += 6
            for win in WIN:
                if win[0] == player1:
                    total_score += SHAPE[win[2]]
                    break
    print(total_score)


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    part1(data)
    part2(data)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=2)
    solve(puzzle.input_data)
