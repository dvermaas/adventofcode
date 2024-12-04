from typing import List
from aocd import get_data

data = get_data(day=4, year=2024).splitlines()


def part_1(puzzle_data: List[str], substring: str = "XMAS") -> int:
    out = 0
    window = len(substring)
    for y, row in enumerate(puzzle_data):
        for x, item in enumerate(row):
            out += sum([
                row[x: x + window] == substring if x + window <= len(row) else False,
                row[x: x + window] == substring[::-1] if x + window <= len(row) else False,
                ''.join([puzzle_data[y+i][x] for i in range(window)]) == substring if y + window <= len(puzzle_data) else False,
                ''.join([puzzle_data[y+i][x] for i in range(window)]) == substring[::-1] if y + window <= len(puzzle_data) else False,
                ''.join([puzzle_data[y+i][x+i] for i in range(window)]) == substring if y + window <= len(puzzle_data) and x + window <= len(row) else False,
                ''.join([puzzle_data[y+i][x+i] for i in range(window)]) == substring[::-1] if y + window <= len(puzzle_data) and x + window <= len(row) else False,
                ''.join([puzzle_data[y - i][x + i] for i in range(window)]) == substring if y - window + 1 >= 0 and x + window <= len(row) else False,
                ''.join([puzzle_data[y - i][x + i] for i in range(window)]) == substring[::-1] if y - window + 1 >= 0 and x + window <= len(row) else False,
            ])
    return out


def part_2(puzzle_data: List[str]):
    out = 0
    for y in range(1, len(puzzle_data)-1):
        for x in range(1, len(puzzle_data[0])-1):
            if not puzzle_data[y][x] == "A":
                continue

            d1, d2 = puzzle_data[y+1][x-1], puzzle_data[y-1][x+1]
            d3, d4 = puzzle_data[y+1][x+1], puzzle_data[y-1][x-1]
            if {d1, d2} != {"M", "S"} or {d3, d4} != {"M", "S"}:
                continue
            out += 1
    return out


print(f"Part 1: {part_1(data)}")
print(f"Part 2: {part_2(data)}")
