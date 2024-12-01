from typing import Tuple

data = open("data/day5t.txt").read().split("\n\n")


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
parsed_data = parsed_data[:]


def solve(intitial_range: list):
    queue = [intitial_range]
    out = []
    while queue:
        depth, destination, source, length = queue.pop()
        end = source + length
        for layer_destination, layer_source, layer_length in parsed_data[depth]:
            layer_shift = layer_destination - layer_source
            layer_end = layer_source + layer_length
            if source >= layer_source and end <= layer_end:
                queue.append([1, destination + layer_shift, source, layer_length])
                
        

def setup(seed_list: list, ranges=False):
        seed_list = [item for seed in seed_list for item in (seed, 1)] if not ranges else seed_list
        for i in range(0, len(seed_list), 2):
            solve([0, seed_list[i], seed_list[i], seed_list[i]+1])
            


print(setup(seeds))
    