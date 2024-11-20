data = open("day5.txt").read().splitlines()


def parser() -> list:
    out = []
    sub_out = []
    for line in data:
        if len(line) > 0:
            sub_out.append(line)
        else:
            out.append(sub_out)
            sub_out = []
    out[0] = out[0][0].split(": ")
    out = [
        [list(map(int, line.split(" "))) for line in group[1:]]
        for group in out
    ]
    out[0] = out[0][0]
    return out


parsed_data = parser()


def data_hasher(data_index: int) -> dict:
    hashmap = {}
    for d_range, s_range, length in parsed_data[data_index]:
        for i in range(length):
            hashmap[s_range + i] = d_range + i
    return hashmap


hash_dict = [data_hasher(i) for i in range(1, len(parsed_data))]


def data_farmer(seed: int) -> int:
    out = seed
    for i in range(len(hash_dict)):
        if out in hash_dict[i]:
            out = hash_dict[i][out]
    return out
    

def calculate_lowest_location():
    return min([data_farmer(seed) for seed in parsed_data[0]])
    
    
print(f"Part 1: {calculate_lowest_location()}")
# print(data_farmer(79))
# print(data_farmer(14))
# print(data_farmer(55))
# print(data_farmer(13))
