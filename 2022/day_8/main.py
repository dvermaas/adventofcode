def is_visible(forest_data: list, i: int, j: int) -> bool:
    height = forest_data[i][j]
    forest_hor = forest_data[i]
    forest_vert = [forest_data[z][j]for z in range(len(forest_data))]
    max_heights = [max(forest_vert[:i]), max(forest_hor[j+1:]), max(forest_vert[i+1:]), max(forest_hor[:j])]
    return sum([direction_height < height for direction_height in max_heights]) > 0


def calculate_total_visible(forest_data: list):
    forest = []
    for tree_line in forest_data:
        forest.append([int(tree) for tree in tree_line])

    total_visible = 0
    for i in range(1, len(forest) - 1):
        for j in range(1, len(forest[0]) - 1):
            total_visible += is_visible(forest, i, j)
    border_trees = 2 * (len(forest) + len(forest[0]) - 2)
    return total_visible + border_trees


forest_data = open("input.txt").read().splitlines()
print(f"Part 1: {calculate_total_visible(forest_data)}")


def visibility_score(forest_data: list, i: int, j: int) -> int:
    height = forest_data[i][j]
    vertical = [forest_data[z][j] for z in range(len(forest_data))]
    x_left, x_right = list(forest_data[i][:j].__reversed__()), forest_data[i][j+1:]
    y_left, y_right = list(vertical[:i].__reversed__()), vertical[i+1:]
    total_score = 1
    for tree_line in (x_left, x_right, y_left, y_right):
        for score, tree_height in enumerate(tree_line, 1):
            if tree_height >= height or score == len(tree_line):
                total_score *= score
                break
    return total_score


def calculate_visibility_scores(forest_data: list):
    forest = []
    for tree_line in forest_data:
        forest.append([int(tree) for tree in tree_line])

    current_highscore, best_i, best_j = 0, 0, 0
    for i in range(1, len(forest) - 1):
        for j in range(1, len(forest[0]) - 1):
            score = visibility_score(forest, i, j)
            if score > current_highscore:
                current_highscore, best_i, best_j = score, i, j
    return current_highscore, best_i, best_j


print(f"Part 2: {calculate_visibility_scores(forest_data)[0]}")
