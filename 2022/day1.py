from aocd import get_data

calories_list = get_data(day=1, year=2022).splitlines()

elf_calories_list = []
total = 0
for item in calories_list:
    if item == "":
        elf_calories_list.append(total)
        total = 0
    else:
        total += int(item)

print(f"Max calories elf: {max(elf_calories_list)}")
print(f"Total calories top three elves: {sum(sorted(elf_calories_list)[-3:])}")