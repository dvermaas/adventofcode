data = open("day5t.txt").read().splitlines()


def parser():
    out = []
    sub_out = []
    for line in data:
        if len(line) > 0:
            sub_out.append(line)
        else:
            out.append(sub_out)
            sub_out = []
    out[0] = out[0][0].split(": ")
    print(out[0][1].split(" "))
    out = [
        [list(map(int, line.split(" "))) for line in group[1:]]
        for group in out
    ]
    return out


print(parser())
