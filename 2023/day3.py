data = open("day3.txt").read().splitlines()


def is_special_char_around(y, sx, x):
    for row in data[max(0, y-1):y+2]:
        for item in row[max(0, sx-1):x+1]:
            if item != '.' and not item.isdigit():
                return True
    return False


def calculate_part_sum():
    out = 0
    for y, row in enumerate(data):
        x = 0
        while x < len(row):
            if row[x].isnumeric():
                sx = x
                while x < len(row) and row[x].isdigit():
                    x += 1
                if is_special_char_around(y, sx, x):
                    out += int(row[sx:x])
            x += 1
    return out


print(f"Part 1: {calculate_part_sum()}")
