import re
from typing import List
from itertools import product
from tqdm import tqdm

from aocd import get_data

data = get_data(day=7, year=2024).splitlines()


def lr_eval(math: str) -> int:
    tokens = re.split(r'(\+|\*|\|\|)', math)
    # print(f"{tokens=}")
    if len(tokens) < 3:
        return eval(math)
    if tokens[1] == "||":
        return lr_eval(tokens[0]+tokens[2] + "".join(tokens[3:]))
    return lr_eval(str(eval("".join(tokens[:3]))) + "".join(tokens[3:]))


def part_1(puzzle_data: List[str], chars: tuple = ("+", "*")):
    out = 0
    for line in tqdm(puzzle_data):
        result, numbers = line.split(": ")
        result, numbers = int(result), numbers.split(" ")
        prod_list = list(product(chars, repeat=len(numbers)-1))
        for prod in prod_list:
            if lr_eval("".join(a+b for a, b in zip(numbers, prod)) + numbers[-1]) == result:
                out += result
                break
    return out
        
        
print("part 1:", part_1(data)) # 3749
print("part 2:", part_1(data, chars=("+", "*", "||")))
