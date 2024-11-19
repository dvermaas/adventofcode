data = open("day1.txt").read().splitlines()


numbers = ["one", "two", "three", "four", "five",
           "six", "seven", "eight", "nine"]


def sum_first_last_int(lines: list) -> int:
    total = 0
    for line in lines:
        digits = [char for char in line if char.isdigit()]
        total += int(digits[0] + digits[-1])
    return total


def replace_strings(lines: list) -> list:
    output_lines = []
    for line in lines:
        for i, number_str in enumerate(numbers, 1):
            line = line.replace(number_str, f"{number_str[0] + str(i) + number_str[-1]}")
        output_lines.append(line)
    return output_lines


print(f"Part 1: {sum_first_last_int(data)}")
print(f"Part 2: {sum_first_last_int(replace_strings(data))}")