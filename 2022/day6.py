from aocd import get_data

coms = get_data(day=6, year=2022)


def find_marker(data: str, window_size: int) -> int:
    for i in range(len(data) - window_size):
        data_window = data[i:i+window_size]
        if len(set(data_window)) == window_size:
            return i + window_size


print(f"Marker location (window=4): {find_marker(coms, 4)}")
print(f"Marker location (window=14): {find_marker(coms, 14)}")

