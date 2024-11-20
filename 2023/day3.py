import math
from collections import defaultdict
from typing import Optional

data = open("day3.txt").read().splitlines()


def is_special_char_around(y, sx, x) -> bool:
    for row in data[max(0, y - 1): y + 2]:
        for item in row[max(0, sx - 1): x + 1]:
            if item != "." and not item.isdigit():
                return True
    return False


def calculate_part_sum() -> int:
    out = 0
    for y, row in enumerate(data):
        x = 0
        while x < len(row):
            if row[x].isnumeric():
                sx = x
                while x < len(row) and row[x].isdigit():
                    x += 1
                if is_special_char_around(y, sx, x):
                    out += int(row[sx:x])
            x += 1
    return out


def is_gear_around(y, sx, x) -> Optional[tuple]:
    for gy, row in enumerate(data[max(0, y - 1): y + 2]):
        for gx, item in enumerate(row[max(0, sx - 1): x + 1]):
            if item == "*":
                return max(0, y - 1) + gy, max(0, sx - 1) + gx


def calculate_gear_sum() -> int:
    gear_dict = defaultdict(list)
    for y, row in enumerate(data):
        x = 0
        while x < len(row):
            if row[x].isnumeric():
                sx = x
                while x < len(row) and row[x].isdigit():
                    x += 1
                coords = is_gear_around(y, sx, x)
                if coords:
                    gear_dict[coords].append(int(row[sx:x]))  
            x += 1
    return sum([math.prod(values) for values in gear_dict.values() if len(values) > 1])


print(f"Part 1: {calculate_part_sum()}")
print(f"Part 2: {calculate_gear_sum()}")
