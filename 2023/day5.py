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

print(f"{seeds=}")
for row in parsed_data:
    print(row)


# def recursive_solve(depth, source, destination, length):
#     print("debug", depth, source, destination, length)
#     out = []
#     end_source = source + length
#     if depth >= len(parsed_data):
#         return [source, destination, length]
# 
#     for p_source, p_destination, p_length in parsed_data[depth]:
#         print("checking", [p_source, p_destination, p_length])
#         p_end_source = p_source + p_length
# 
#         if p_source <= source and end_source <= p_end_source:
#             print("trigger 1")
#             # Condition 1: Entire segment fits within p_source to p_end_source.
#             return [recursive_solve(depth + 1, source, p_destination, length)]
# 
#         elif p_source < end_source <= p_end_source:
#             # Condition 2: Segment partially outside at the start.
#             outside = p_source - source
#             print("trigger 2", outside)
#             return [
#                 recursive_solve(depth, source, destination, outside),
#                 recursive_solve(depth + 1, p_source, p_destination, length - outside)
#             ]
# 
#         elif p_source <= source <= p_end_source:
#             # Condition 3: Segment partially outside at the end.
#             inside = source - p_end_source
#             print("trigger 3", f"{inside=} {length=}, {source=}, {p_end_source=}")
#             return [
#                 recursive_solve(depth + 1, source, p_destination, inside),
#                 recursive_solve(depth, source, p_destination, length - inside)
#             ]
#         print("trigger pass")
# 
#     return [source, destination, length]
def recursive_solve(depth, source, destination, length):
    print("debug", depth, source, destination, length)
    end_source = source + length
    if depth >= len(parsed_data):  # Base case: stop recursion if depth exceeds data length
        return [source, destination, length]

    for p_source, p_destination, p_length in parsed_data[depth]:
        print("checking", [p_source, p_destination, p_length])
        p_end_source = p_source + p_length

        if p_source <= source and end_source <= p_end_source:
            print("trigger 1")  # Entire segment is contained
            return [recursive_solve(depth + 1, source, p_destination, length)]

        elif source < p_source < end_source <= p_end_source:
            print("trigger 2")  # Partially outside at the start
            outside = p_source - source
            return [
                recursive_solve(depth, source, destination, outside),
                recursive_solve(depth + 1, p_source, p_destination, length - outside)
            ]

        elif p_source <= source < p_end_source < end_source:
            print("trigger 3")  # Partially outside at the end
            inside = p_end_source - source
            return [
                recursive_solve(depth + 1, source, p_destination, inside),
                recursive_solve(depth, p_end_source, destination, length - inside)
            ]

        print("trigger pass")  # Debug when no condition matches

    return recursive_solve(depth + 1, source, destination, length)


for i in range(0, len(seeds), 2):
    print()
    print("Starting sequence")
    print('solve', recursive_solve(0, seeds[i], seeds[i], seeds[i + 1]))
    