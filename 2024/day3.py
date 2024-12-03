from typing import List, Tuple
from aocd import get_data
import re
data = open('day3t.txt').read().splitlines()
data = get_data(day=3, year=2024)


def part_1(puzzle_data: List[str]):
    out = 0
    for line in puzzle_data:
        multiplications = [list(map(int, mul[4:-1].split(","))) for mul in re.findall(r"mul\(\d+,\d+\)", line)]
        out += sum([a*b for a, b in multiplications])
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
    print(do_list, not_list)
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


def part_2(puzzle_data: List[str]) -> int:
    out = 0
    for line in puzzle_data:
        multiplications = re.findall(r"mul\(\d+,\d+\)", line)
        mult_indexes = [line.index(mul) for mul in multiplications]
        print(f"{mult_indexes=}")
        ranges = get_do_ranges(line)
        print(f"{ranges=}")
        multiplied = [a * b for a, b in [list(map(int, mul[4:-1].split(","))) for mul in multiplications]]
        for index, total in zip(mult_indexes, multiplied):
            for i in range(0, len(ranges), 2):
                if ranges[i] < index < ranges[i+1]:
                    print(f"adding {index} because it is within {ranges[i], ranges[i+1]}")
                    out += total
                    break
    return out


# 108827062 is too high
# 78567818 is incorrect
# 77055967 was correct
# 67904534 is too low
print(f"Part 1: {part_1(data)}")
print(f"Part 2: {part_2(data)}")
