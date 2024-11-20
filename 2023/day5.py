from typing import Tuple

data = open("data/day5.txt").read().splitlines()


def parser() -> Tuple[list, list]:
    out = []
    sub_out = []
    for line in data:
        if len(line) > 0:
            sub_out.append(line)
        else:
            out.append(sub_out)
            sub_out = []
    out.append(sub_out)
    out[0] = out[0][0].split(": ")
    out = [
        [list(map(int, line.split(" "))) for line in group[1:]]
        for group in out
    ]
    return out[0][0], out[1:]


seeds, parsed_data = parser()
for row in parsed_data:
    print(row)
    
    
def fast_converter(data_index: int, seed: int) -> int:
    for d_range, s_range, length in parsed_data[data_index]:
        if seed in range(s_range, s_range + length):
            return seed + (d_range - s_range)
    return seed


print(fast_converter(0, 79))


def calculate_location(seed: int) -> int:
    debug = [seed]
    out = seed
    for i in range(len(parsed_data)):
        out = fast_converter(i, out)
        debug.append(out)
    print('debug', debug)
    return out
        

def calculate_lowest_location():
    return min([calculate_location(seed) for seed in seeds])
    
    
print(f"Part 1: {calculate_lowest_location()}")
