from typing import List, Tuple
from collections import Counter


def parse(puzzle_input: List[str]) -> Tuple[List[int], List[int]]:
    left = []
    right = []
    for line in puzzle_input:
        a, b = line.split()
        left.append(int(a))
        right.append(int(b))
    return left, right


def part1(left: List[int], right: List[int]) -> int:
    out = 0
    for a, b in zip(sorted(left), sorted(right)):
        out += abs(a - b)
    return out


def part2(left: List[int], right: List[int]) -> int:
    out = 0
    count_dict = Counter(right)
    for item in left:
        if item in count_dict:
            out += item * count_dict[item]
    return out
    
    
left_data, right_data = parse(open("data/day1.txt").read().splitlines())
print(f"Part 1: {part1(left_data, right_data)}")
print(f"Part 2: {part2(left_data, right_data)}")
