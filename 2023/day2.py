from collections import defaultdict
from aocd import get_data

data = get_data(day=2, year=2023).splitlines()
rgb_total = {"red": 12, "green": 13, "blue": 14}


def is_game_valid(game, rgb_limit: dict) -> bool:
    _, game_data = game.split(":")
    for sub_game in game_data.split(";"):
        for cube_data in sub_game.split(","):
            _, number, color = cube_data.split(" ")
            if rgb_limit[color] < int(number):
                return False
    return True


def valid_game_parser(games: list, rgb_limit: dict) -> int:
    out = 0
    for i, game in enumerate(games, 1):
        if is_game_valid(game, rgb_limit):
            out += i
    return out


def minimal_games(games: list) -> int:
    out = 0
    for i, game in enumerate(games, 1):
        _, game_data = game.split(":")
        min_colors = defaultdict(int)
        for sub_game in game_data.split(";"):
            for cube_data in sub_game.split(","):
                _, number, color = cube_data.split(" ")
                number = int(number)
                if min_colors[color] < number:
                    min_colors[color] = number

        game_value = 1
        for value in min_colors.values():
            game_value *= value
        out += game_value
    return out


print(f"Part 1: {valid_game_parser(data, rgb_total)}")
print(f"Part 2: {minimal_games(data)}")
