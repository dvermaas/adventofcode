from typing import List


def parse(puzzle_input: List[str]) -> List[List[int]]:
    return [[int(number) for number in line.split()] for line in puzzle_input]
    
    
def is_save(report: List[int], dampener: int) -> bool:
    if report[1] < report[0]:
        report.reverse()
    for i in range(len(report) - 1):
        delta = report[i+1] - report[i]
        if delta < 1 or delta > 3:
            if dampener > 0:
                dampener -= 1
                continue
            return False
    return True


def report_calculator(puzzle_input: List[List[int]], dampener=0) -> int:
    return sum([is_save(line, dampener) for line in puzzle_input])
        

data = parse(open("data/day2.txt").read().splitlines())
print(f"Part 1: {report_calculator(data)}")
print(f"Part 2: {report_calculator(data, dampener=1)}")
