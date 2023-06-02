sections = open("input.txt").read().splitlines()
parsed_sections = []
for section in sections:
    elf0 = list(map(int, section.split(",")[0].split("-")))
    elf1 = list(map(int, section.split(",")[1].split("-")))
    parsed_sections.append([min(elf0), max(elf0), min(elf1), max(elf1)])


def section_parser(section: str):
    elf0_s, elf0_e, elf1_s, elf1_e = section
    if elf0_s <= elf1_s and elf1_e <= elf0_e:
        return 1
    if elf1_s <= elf0_s and elf0_e <= elf1_e:
        return 1
    return 0


print(f"Number of contained pairs: {sum([section_parser(section) for section in parsed_sections])}")


def is_general_overlap(section: str):
    elf0_s, elf0_e, elf1_s, elf1_e = section
    overlap_set = set(range(elf0_s, elf0_e + 1)).intersection(range(elf1_s, elf1_e + 1))
    if len(overlap_set) > 0:
        return 1
    return 0


print(f"Number of overlapping pairs: {sum([is_general_overlap(section) for section in parsed_sections])}")
