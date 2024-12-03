from typing import List
from aocd import get_data
import re

data = get_data(day=3, year=2024)


def part_1(puzzle_data: str):
    out = 0
    multiplications = [list(map(int, mul[4:-1].split(","))) for mul in re.findall(r"mul\(\d+,\d+\)", puzzle_data)]
    out += sum([a * b for a, b in multiplications])
    return out


def find_all_indexes(line: str, substring: str) -> List[int]:
    out = []
    substring_length = len(substring)
    start = 0
    while True:
        start = line.find(substring, start)
        if start == -1:
            break
        out.append(start)
        start += substring_length
    return out


def get_do_ranges(line: str) -> List[int]:
    out = [0]
    do_list = [0] + find_all_indexes(line, "do()")
    not_list = find_all_indexes(line, "don't()")
    is_active = True
    while True:
        if is_active:
            if not not_list:
                out.append(len(line))
                break
            next_index = not_list.pop(0)
        else:
            if not do_list:
                out.append(len(line))
                break
            next_index = do_list.pop(0)
        if next_index > out[-1]:
            out.append(next_index)
            is_active = not is_active
    return out


def part_2(puzzle_data: str) -> int:
    out = 0
    multiplications = re.findall(r"mul\(\d+,\d+\)", puzzle_data)
    mult_indexes = [puzzle_data.index(mul) for mul in multiplications]
    ranges = get_do_ranges(puzzle_data)
    multiplied = [a * b for a, b in [list(map(int, mul[4:-1].split(","))) for mul in multiplications]]
    for index, total in zip(mult_indexes, multiplied):
        for i in range(0, len(ranges), 2):
            if ranges[i] < index < ranges[i + 1]:
                out += total
                break
    return out


print(f"Part 1: {part_1(data)}")
print(f"Part 2: {part_2(data)}")
