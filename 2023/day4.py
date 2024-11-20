import re
from collections import defaultdict

data = open("day4.txt").read().splitlines()


def calculate_score():
    total = 0
    for row in data:
        match = re.match(r".*:\s*([\d\s]+)\|\s*([\d\s]+)", row)
        left_numbers = set(map(int, match.group(1).split()))
        right_numbers = set(map(int, match.group(2).split()))
        winning_numbers = left_numbers & right_numbers
        if winning_numbers:
            score = 2 ** (len(winning_numbers) - 1)
            total += score
    return total


def new_rules_score():
    total = 0
    clones = defaultdict(int)
    for game, row in enumerate(data, 1):
        match = re.match(r".*:\s*([\d\s]+)\|\s*([\d\s]+)", row)
        left_numbers = set(map(int, match.group(1).split()))
        right_numbers = set(map(int, match.group(2).split()))
        winning_numbers = left_numbers & right_numbers
        for i in range(1, len(winning_numbers) + 1):
            clones[game + i] += 1 + clones[game]
        total += 1
    return total + sum(clones.values())


print(f"Part 1: {calculate_score()}")
print(f"Part 2: {new_rules_score()}")
