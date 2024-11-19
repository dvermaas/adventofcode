data = open("day3t.txt").read().splitlines()


def is_special_char_around(y, sx, x):
    print("Checking:", data[y][sx:x])
    for row in data[max(0, y-1):y+2]:
        print("row", row[max(0, sx-1):x+1])
        for item in row[max(0, sx-1):x+1]:
            if item != '.' and not item.isdigit():
                # return True
                pass
    return False


def find_the_numbers():
    out = 0
    for y, row in enumerate(data):
        x = 0
        while x < len(row):
            if row[x].isnumeric():
                sx = x
                while x < len(row) and row[x].isdigit():
                    x += 1
                print("hmmm", (sx, x))
                if is_special_char_around(y, sx, x):
                    out += int(row[sx:x])
            x += 1
    return out


# 564267 is too high?
print(f"Part 1: {find_the_numbers()}")
