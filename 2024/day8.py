import copy
from collections import defaultdict
from typing import List
from itertools import combinations

from aocd import get_data

# data = [[item for item in line] for line in open("day6.txt").read().splitlines()]
data = [[item for item in line] for line in get_data(day=8, year=2024).splitlines()]


def find_locations(puzzle_input: List[List[str]]) -> defaultdict:
    locations = defaultdict(list)
    for y, line in enumerate(puzzle_input):
        for x, item in enumerate(line):
            if item != ".":
                locations[item].append((y, x))
    return locations


def part_1(puzzle_input: List[List[str]]) -> int:
    puzzle_input = copy.deepcopy(puzzle_input)
    out = 0
    locations = find_locations(puzzle_input)
    for k, v in locations.items():
        for combination in combinations(v, 2):
            (y1, x1), (y2, x2) = combination
            dy, dx = y2 - y1, x2 - x1

            if 0 <= y1 - dy < len(puzzle_input) and 0 <= x1 - dx < len(puzzle_input[0]):
                if not puzzle_input[y1 - dy][x1 - dx] == "#":
                    puzzle_input[y1 - dy][x1 - dx] = "#"
                    out += 1

            if 0 <= y2 + dy < len(puzzle_input) and 0 <= x2 + dx < len(puzzle_input[0]):
                if not puzzle_input[y2 + dy][x2 + dx] == "#":
                    puzzle_input[y2 + dy][x2 + dx] = "#"
                    out += 1
    return out


print("part 1:", part_1(data))
# print("part 2:", part_2(data))
