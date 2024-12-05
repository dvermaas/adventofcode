from aocd import get_data
from collections import defaultdict

data = get_data(day=5, year=2024)


def parser(puzzle_input: str):
    puzzle_input = puzzle_input.split("\n\n")
    hashmap = defaultdict(list)
    for item in puzzle_input[0].splitlines():
        x, y = map(int, item.split("|"))
        hashmap[x].append(y)
    pages = [list(map(int, item.split(","))) for item in puzzle_input[1].splitlines()]
    return hashmap, pages


def page_solver(hashmap: defaultdict, page: list) -> int:
    for i, item in enumerate(page):
        for dependency in hashmap[item]:
            if dependency in page and dependency not in page[i:]:
                return 0
    return page[len(page)//2]


def part_1(parsed_data: tuple) -> int:
    out = 0
    hashmap, pages = parsed_data
    for page in pages:
        out += page_solver(hashmap, page)
    return out


def page_fixer(hashmap: defaultdict, page: list) -> list:
    for i, item in enumerate(page):
        for dependency in hashmap[item]:
            if dependency in page and dependency not in page[i:]:
                dep = page.pop(page.index(dependency))
                page.append(dep)
                return page_fixer(hashmap, page)
    return page


def page_fixer_inline(hashmap: defaultdict, page: list) -> list:
    i = 0
    while i < len(page):
        for dependency in hashmap[page[i]]:
            if dependency in page and page.index(dependency) < i:
                i = page.index(dependency)
                page.pop(i)
                page.append(dependency)
                i -= 1
                break
        i += 1
    return page


def part_2(parsed_data: tuple) -> int:
    out = 0
    hashmap, pages = parsed_data
    for page in pages:
        if not page_solver(hashmap, page):
            out += page_fixer(hashmap, page)[len(page)//2]
    return out


print("part 1:", part_1(parser(data)))
print("part 2:", part_2(parser(data)))
