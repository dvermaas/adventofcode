from typing import List, Tuple

from aocd import get_data

data = [list(line) for line in open("day6.txt").read().splitlines()]


def find_guard(puzzle_input: List[List[str]]) -> Tuple[int, int]:
    guard = ("^", ">", "v", "<")
    for y, line in enumerate(puzzle_input):
        for x, item in enumerate(line):
            if item in guard:
                return y, x


def print_puzzle(puzzle_input: List[List[str]]):
    for line in puzzle_input:
        print("".join(line))


def move_guard(puzzle_input: List[List[str]], guard_location: Tuple[int, int]):
    print("debug", part_1(puzzle_input))
    if part_1(puzzle_input) == 962:
        print_puzzle(puzzle_input)
    guard = ("^", ">", "v", "<")
    offsets = ((-1, 0), (0, 1), (1, 0), (0, -1))
    y, x = guard_location
    index = guard.index(puzzle_input[y][x])
    dy, dx = offsets[index]
    if not 0 <= y+dy < len(puzzle_input) or not 0 <= x+dx < len(puzzle_input[0]):
        return puzzle_input
    if puzzle_input[y+dy][x+dx] == "#":
        puzzle_input[y][x] = guard[(index + 1) % 4]
        return move_guard(puzzle_input, guard_location)
    puzzle_input[y+dy][x+dx] = puzzle_input[y][x]
    puzzle_input[y][x] = "X"
    return move_guard(puzzle_input, (y+dy, x+dx))


def part_1(puzzle_input: List[List[str]]) -> int:
    out = 0
    for line in puzzle_input:
        for item in line:
            if item == "X":
                out += 1
    return out + 1


print_puzzle(move_guard(data, find_guard(data)))
print(part_1(move_guard(data, find_guard(data))))
