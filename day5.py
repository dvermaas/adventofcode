from aocd import get_data
from collections import defaultdict

# data = open("lol.txt").read()
data = get_data(day=5, year=2024)

def parser(puzzle_input: str):
    puzzle_input = puzzle_input.split("\n\n")
    hashmap = defaultdict(list)
    for item in puzzle_input[0].splitlines():
        x, y = map(int, item.split("|"))
        hashmap[x].append(y)
    pages = [tuple(map(int, item.split(","))) for item in puzzle_input[1].splitlines()]
    return hashmap, pages

def part_1(parsed_data: tuple) -> int:
    def page_solver(hashmap, page) -> int:
        print(hashmap)
        print(page)
        for i, item in enumerate(page):
            for dependency in hashmap[item]:
                print(f"{dependency=}")
                if dependency in page and dependency not in page[i:]:
                    return 0
        return page[len(page)//2]

    out = 0
    hashmap, pages = parsed_data
    for page in pages:
        out += page_solver(hashmap, page)
    return out

print(part_1(parser(data)))
