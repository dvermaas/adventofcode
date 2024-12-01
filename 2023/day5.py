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


def recursive_solve(depth, destination, source, length):
    print("debug", depth, [destination, source, length])
    end_source = source + length

    # Base case: If we reach the maximum depth, return the destination
    if depth >= len(parsed_data):
        return [destination]

    results = []  # Store results of recursive calls

    for p_destination, p_source, p_length in parsed_data[depth]:
        p_end_source = p_source + p_length
        shift = p_destination - p_source
        print('tts', p_source <= source, p_source, source, end_source <= p_end_source, end_source, p_end_source)
        if p_source <= source and end_source <= p_end_source:
            print(f"trigger 1 {shift=}, {[p_destination, p_source, p_length]}")
            results.extend(recursive_solve(depth + 1, destination + shift, source, length))
            break
        elif source < p_destination < end_source <= p_end_source:
            print("trigger 2")  # Partially outside at the start
            outside = p_destination - source
            results.extend(recursive_solve(depth, destination, source, outside))
            results.extend(recursive_solve(depth + 1, p_destination, p_source, length - outside))
            break
        elif p_destination <= source < p_end_source < end_source:
            print("trigger 3")  # Partially outside at the end
            inside = p_end_source - source
            results.extend(recursive_solve(depth + 1, source, p_source, inside))
            results.extend(recursive_solve(depth, destination, p_end_source, length - inside))
            break
    if not results:
        results.extend(recursive_solve(depth + 1, destination,source , length))
    return results


for i in range(0, len(seeds), 2):
    print()
    print("Starting sequence")
    print('solve', min(recursive_solve(0, seeds[i], seeds[i], seeds[i + 1])))
    