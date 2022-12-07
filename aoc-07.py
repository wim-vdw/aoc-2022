from aocd.models import Puzzle
from collections import defaultdict


def parse(puzzle_input):
    """Parse input."""
    return [line for line in puzzle_input.split('\n')]


def handle_data_for_part1_and_part2(puzzle_input):
    current_dir = '/'
    files = []
    for line in puzzle_input:
        if line.startswith('$'):
            command = line.split()
            if command[1] == 'cd':
                target_dir = command[2]
                if target_dir == '/':
                    current_dir = '/'
                elif target_dir == '..':
                    tmp = list(x for x in current_dir.split('/') if x)
                    current_dir = '/'
                    if len(tmp) > 1:
                        for i in range(len(tmp) - 1):
                            current_dir += tmp[i] + '/'
                else:
                    current_dir += target_dir + '/'
        else:
            file = line.split()
            if file[0] != 'dir':
                files.append((file, current_dir))
    dirs = defaultdict(int)
    for file in files:
        directory = file[1]
        filesize = int(file[0][0])
        tmp = list(x for x in directory.split('/') if x)
        if tmp:
            tmp_dir = '/'
            dirs[tmp_dir] += filesize
            for subdir in tmp:
                tmp_dir += subdir + '/'
                dirs[tmp_dir] += filesize
        else:
            dirs[directory] += filesize
    return dirs


def part1(puzzle_input):
    """Solve part 1."""
    dirs = handle_data_for_part1_and_part2(puzzle_input)
    result = 0
    for dir_size in dirs.values():
        if dir_size <= 100000:
            result += dir_size
    print(result)


def part2(puzzle_input):
    """Solve part 2."""
    dirs = handle_data_for_part1_and_part2(puzzle_input)
    unused = 70000000 - dirs['/']
    sizes = [x for x in dirs.values()]
    for size in sorted(sizes):
        if size + unused >= 30000000:
            print(size)
            break


def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    part1(data)
    part2(data)


if __name__ == '__main__':
    puzzle = Puzzle(year=2022, day=7)
    solve(puzzle.input_data)
