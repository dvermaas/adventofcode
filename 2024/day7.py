from typing import List
from itertools import product
from tqdm import tqdm

from aocd import get_data

data = get_data(day=7, year=2024).splitlines()


def lr_eval(result: int, math: List[str]):
    for i in range(1, len(math), 2):
        if math[i] == "+":
            math[i+1] = str(int(math[i-1]) + int(math[i+1]))
        if math[i] == "*":
            math[i+1] = str(int(math[i-1]) * int(math[i+1]))
        if math[i] == "||":
            math[i+1] = math[i-1] + math[i+1]
    return int(math[-1]) == result


def part_1(puzzle_data: List[str], chars: tuple = ("+", "*")):
    out = 0
    for line in tqdm(puzzle_data):
        result, numbers = line.split(": ")
        result, numbers = int(result), numbers.split(" ")
        prod_list = list(product(chars, repeat=len(numbers)-1))
        for prod in prod_list:
            if lr_eval(result, [item for pair in zip(numbers, prod) for item in pair] + [numbers[-1]]):
                out += result
                break
    return out
        
        
print("part 1:", part_1(data))
print("part 2:", part_1(data, chars=("+", "*", "||")))
