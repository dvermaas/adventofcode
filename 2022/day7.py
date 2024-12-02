from aocd import get_data


class Folder:
    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent
        self.children = {}
        self.size = 0
        if parent is not None:
            parent.children[name] = self

    def __str__(self):
        return self.name

    def increase_size(self, size: int):
        self.size += size
        if self.parent is not None:
            self.parent.increase_size(size)


class File:
    def __init__(self, name: str, parent: Folder, size: int):
        self.name = name
        self.parent = parent
        self.size = size
        parent.increase_size(size)


def build_filesystem(commands: list) -> Folder:
    root_folder = Folder(name="Home", parent=None)
    current_folder = root_folder
    for command in commands:
        match command.split():
            case ["$", "ls"]:
                continue
            case["$", "cd", "/"]:
                current_folder = root_folder
            case ["$", "cd", ".."]:
                current_folder = current_folder.parent
            case ["$", "cd", name]:
                if name in current_folder.children:
                    current_folder = current_folder.children[name]
                else:
                    raise ValueError(f"{name} does not exist in directory")
            case ["dir", name]:
                if name not in current_folder.children:
                    Folder(name=name, parent=current_folder)
            case [size, name]:
                File(name=name, parent=current_folder, size=int(size))

    return root_folder


def recursive_find(folder: Folder) -> dict:
    sizes_dict = {folder: folder.size}
    for child in folder.children.values():
        if isinstance(child, Folder):
            sizes_dict.update(recursive_find(child))
    return sizes_dict


commands = get_data(day=7, year=2022).splitlines()
file_system = build_filesystem(commands)
print(f"Part 1: {sum({folder: size for folder, size in recursive_find(file_system).items() if 100000 > size}.values())}")


FS_SIZE = 70000000
FS_UPDATE_SIZE = 30000000
FS_NEEDED = FS_UPDATE_SIZE - (FS_SIZE - file_system.size)
items = {folder: size for folder, size in recursive_find(file_system).items() if size >= FS_NEEDED}
minimal_key = min(items, key=items.get)
print("Part 2:", items.get(minimal_key))