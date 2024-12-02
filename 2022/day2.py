from aocd import get_data

strategies = get_data(day=2, year=2022).splitlines()

shape_value = {"X": 1, "Y": 2, "Z": 3}
victory_value = {
    "X": {"A": 3, "B": 0, "C": 6},
    "Y": {"A": 6, "B": 3, "C": 0},
    "Z": {"A": 0, "B": 6, "C": 3}
}


def score(strategy):
    opponent_move, player_move = strategy.split(" ")
    return victory_value[player_move][opponent_move] + shape_value[player_move]


print(f"Total: {sum([score(strategy) for strategy in strategies])}")


state_value = {"X": 0, "Y": 3, "Z": 6}


def score2(strategy):
    opponent_move, player_state = strategy.split(" ")
    for player_move, enemy_move_dict in victory_value.items():
        if enemy_move_dict[opponent_move] == state_value[player_state]:
            return score(f"{opponent_move} {player_move}")


print(f"Total: {sum([score2(strategy) for strategy in strategies])}")
