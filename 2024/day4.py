from typing import List
from aocd import get_data

data = get_data(day=4, year=2024).splitlines()


def part_1(puzzle_data: List[str], substring: str = "XMAS"):
    out = []
    window = len(substring)
    for y, row in enumerate(puzzle_data):
        for x, item in enumerate(row):
            out.append(sum([
                row[x: x + window] == substring if x + window <= len(row) else False,
                row[x: x + window] == substring[::-1] if x + window <= len(row) else False,
                ''.join([puzzle_data[y+i][x] for i in range(window)]) == substring if y + window <= len(puzzle_data) else False,
                ''.join([puzzle_data[y+i][x] for i in range(window)]) == substring[::-1] if y + window <= len(puzzle_data) else False,
                ''.join([puzzle_data[y+i][x+i] for i in range(window)]) == substring if y + window <= len(puzzle_data) and x + window <= len(row) else False,
                ''.join([puzzle_data[y+i][x+i] for i in range(window)]) == substring[::-1] if y + window <= len(puzzle_data) and x + window <= len(row) else False,
                ''.join([puzzle_data[y - i][x + i] for i in range(window)]) == substring if y - window + 1 >= 0 and x + window <= len(row) else False,
                ''.join([puzzle_data[y - i][x + i] for i in range(window)]) == substring[::-1] if y - window + 1 >= 0 and x + window <= len(row) else False,
            ]))
    return sum(out)


print(f"Part 1: {part_1(data)}")
