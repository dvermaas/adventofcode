import math
from typing import Self, NamedTuple


class Vector2(NamedTuple):
    x: int
    y: int

    def __add__(self, other: Self) -> Self:
        return Vector2(self.x + other.x, self.y + other.y)

    def __sub__(self, other: Self) -> Self:
        return Vector2(self.x - other.x, self.y - other.y)

    def euclidean_dist(self, other: Self) -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Node:
    def __init__(self, x: int, y: int, child=None):
        self.position = Vector2(x, y)
        self.child = child
        self.moves = {"U": Vector2(0, 1), "D": Vector2(0, -1), "L": Vector2(-1, 0), "R": Vector2(1, 0)}
        self.history = set()
        self.history.add(self.position)

    def process_input(self, file: list):
        for i, instruction in enumerate(file):
            direction, amount = instruction.split()
            for _ in range(int(amount)):
                self.move(self.moves[direction])

    @property
    def tail_history(self):
        if self.child is None:
            return self.history
        return self.child.tail_history

    def move(self, direction: Vector2):
        self.position += direction
        if self.child is None:
            self.history.add(self.position)
            return
        if self.position.euclidean_dist(self.child.position) < 2:
            return
        old_parent_pos = self.position - direction
        self.child.move(old_parent_pos - self.child.position)


example = """\
R 4
U 4
L 3
D 1
R 4
D 1
L 5
R 2
""".splitlines()

larger_example = """\
R 5
U 8
L 8
D 3
R 17
D 10
L 25
U 20
""".splitlines()

data = open("input.txt").read().splitlines()


def build_rope(n: int = 1):
    prev_node = Node(0, 0)
    for _ in range(n):
        prev_node = Node(0, 0, child=prev_node)
    return prev_node


H = build_rope()
H.process_input(data)
print("part 1:", len(H.tail_history))

tts = larger_example[:2]
print(tts)
H = build_rope(9)
H.process_input(tts)
print("P2 test", H.tail_history)
# 2607

