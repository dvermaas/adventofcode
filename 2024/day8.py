import copy
from collections import defaultdict
from typing import List
from itertools import combinations

from aocd import get_data

data = [[item for item in line] for line in get_data(day=8, year=2024).splitlines()]


def find_locations(puzzle_input: List[List[str]]) -> defaultdict:
    locations = defaultdict(list)
    for y, line in enumerate(puzzle_input):
        for x, item in enumerate(line):
            if item != ".":
                locations[item].append((y, x))
    return locations


def part_1(puzzle_input: List[List[str]]) -> int:
    def place_node(puzzle_input_reference: List[List[str]], y: int, x: int) -> int:
        if 0 <= y < len(puzzle_input_reference) and 0 <= x < len(puzzle_input_reference[0]):
            if not puzzle_input_reference[y][x] == "#":
                puzzle_input_reference[y][x] = "#"
                return 1
        return 0

    puzzle_input = copy.deepcopy(puzzle_input)
    out = 0
    locations = find_locations(puzzle_input)
    for k, v in locations.items():
        for combination in combinations(v, 2):
            (y1, x1), (y2, x2) = combination
            dy, dx = y2 - y1, x2 - x1
            out += place_node(puzzle_input, y1-dy, x1-dx) + place_node(puzzle_input, y2 + dx, x2 + dx)
    return out


def part_2(puzzle_input: List[List[str]]) -> int:
    def can_place_node(puzzle_input_reference: List[List[str]], y: int, x: int) -> bool:
        if 0 <= y < len(puzzle_input_reference) and 0 <= x < len(puzzle_input_reference[0]):
            return True
        return False

    puzzle_input = copy.deepcopy(puzzle_input)
    out = 0
    locations = find_locations(puzzle_input)
    for k, v in locations.items():
        for combination in combinations(v, 2):
            (y1, x1), (y2, x2) = combination
            dy, dx = y2 - y1, x2 - x1

            i = 0
            while can_place_node(puzzle_input, y1 - (dy*i), x1 - (dx*i)):
                if puzzle_input[y1 - (dy*i)][x1 - (dx*i)] != "#":
                    puzzle_input[y1 - (dy * i)][x1 - (dx * i)] = "#"
                    out += 1
                i += 1

            j = 0
            while can_place_node(puzzle_input, y2 + (dy * j), x2 + (dx * j)):
                if puzzle_input[y2 + (dy*j)][x2 + (dx*j)] != "#":
                    puzzle_input[y2 + (dy*j)][x2 + (dx*j)] = "#"
                    out += 1
                j += 1
    return out


print("part 1:", part_1(data))
print("part 2:", part_2(data))
