from typing import Tuple
from tqdm import tqdm

data = open("data/day5.txt").read().split("\n\n")


def parser() -> Tuple[list, list]:
    seed_list = list(map(int, data[0].split(": ")[1].split()))
    conversion_data = []
    for block in data[1:]:
        sub_table = []
        for line in block.splitlines()[1:]:
            sub_table.append(list(map(int, line.split())))
        conversion_data.append(sub_table)
    return seed_list, conversion_data


seeds, parsed_data = parser()
    

def fast_converter(data_index: int, seed: int) -> int:
    for d_range, s_range, length in parsed_data[data_index]:
        if seed in range(s_range, s_range + length):
            return seed + (d_range - s_range)
    return seed


def calculate_location(seed: int) -> int:
    out = seed
    for i in range(len(parsed_data)):
        out = fast_converter(i, out)
    return out
        

def calculate_lowest_location() -> int:
    return min([calculate_location(seed) for seed in seeds])


def calculate_lowest_range_location() -> int:
    out = calculate_location(seeds[0])
    for i in range(0, len(seeds), 2):
        for seed in tqdm(range(seeds[i], seeds[i] + seeds[i + 1])):
            location = calculate_location(seed)
            if location < out:
                out = location
    return out

    
print(f"Part 1: {calculate_lowest_location()}")
print(f"Part 2: {calculate_lowest_range_location()}")
