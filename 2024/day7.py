from typing import List
from itertools import product
from tqdm import tqdm

from aocd import get_data

data = get_data(day=7, year=2024).splitlines()


def is_buildable(result: int, numbers: List[int], operators: List[str]) -> bool:
    out = numbers[0]
    for i, operator in enumerate(operators):
        if operator == "+":
            out += numbers[i+1]
        elif operator == "*":
            out *= numbers[i+1]
        elif operator == "||":
            out = int(str(out) + str(numbers[i+1]))
    return out == result


def part_1(puzzle_data: List[str], chars: tuple = ("+", "*")) -> int:
    out = 0
    for line in tqdm(puzzle_data):
        result, numbers = line.split(": ")
        result, numbers = int(result), list(map(int, numbers.split(" ")))
        operators_list = list(product(chars, repeat=len(numbers)-1))
        for operators in operators_list:
            if is_buildable(result, numbers, operators):
                out += result
                break
    return out
        
        
print("part 1:", part_1(data))
print("part 2:", part_1(data, chars=("+", "*", "||")))
