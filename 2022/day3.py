from aocd import get_data

backpack_list = get_data(day=3, year=2022).splitlines()


def priority(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 38


def find_duplicate_item(inventory: str):
    compartment1 = set(inventory[:len(inventory)//2])
    compartment2 = inventory[len(inventory) // 2:]
    return compartment1.intersection(compartment2).pop()


print(f"Priority sum: {sum([priority(find_duplicate_item(backpack)) for backpack in backpack_list])}")

group_size = 3
group_backpack_lists = [backpack_list[i:i+group_size] for i in range(0, len(backpack_list), group_size)]


def group_intersection(group_backpacks: list):
    set_backpack = set(group_backpacks.pop())
    for backpack in group_backpacks:
        set_backpack = set_backpack.intersection(backpack)
    return set_backpack.pop()


print(f"Priority sum: {sum([priority(group_intersection(group)) for group in group_backpack_lists])}")
