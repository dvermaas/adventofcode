STACKS_WIDTH = 9
STACKS_HEIGHT = 9
STACK_STATE = [[] for _ in range(STACKS_WIDTH)]
containers = open("input.txt").read().splitlines()

for offset in range(1, STACKS_HEIGHT):
    state = [containers[STACKS_HEIGHT-offset-1][i:i+1] for i in range(1, 4 * STACKS_WIDTH, 4)]
    for i, crate in enumerate(state):
        if crate == " ":
            continue
        STACK_STATE[i].append(crate)


def crate_mover_9000(stack_state):
    for instruction in containers[STACKS_HEIGHT + 1:]:
        parsed = instruction.split(" ")
        parsed = [int(parsed[i]) for i in range(1, len(parsed), 2)]
        for amount in range(parsed[0]):
            stack_state[parsed[2] - 1].append(stack_state[parsed[1] - 1].pop())
    return stack_state


print(f"CM9000 top containers: {''.join([stack[-1] for stack in crate_mover_9000(STACK_STATE)])}")


def crate_mover_9001(stack_state):
    for instruction in containers[STACKS_HEIGHT + 1:]:
        parsed = instruction.split(" ")
        parsed = [int(parsed[i]) for i in range(1, len(parsed), 2)]
        stack_state[parsed[2] - 1] += stack_state[parsed[1] - 1][-parsed[0]:]
        stack_state[parsed[1] - 1] = stack_state[parsed[1] - 1][:-parsed[0]]
    return stack_state


print(f"CM9001 top containers: {''.join([stack[-1] for stack in crate_mover_9001(STACK_STATE)])}")
