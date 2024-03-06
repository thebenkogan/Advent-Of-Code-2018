from collections import defaultdict, deque
from aoc import read_input

lines = read_input()


regex = lines[0][1:-1]

# graph representing the room
adj = defaultdict(set)

pos = {(0, 0)}
stack = []
starts, ends = {(0, 0)}, set()

for c in regex:
    if c == "|":
        ends.update(pos)
        pos = starts
    elif c in "NESW":
        dx, dy = {"N": (0, 1), "E": (1, 0), "S": (0, -1), "W": (-1, 0)}[c]
        for x, y in pos:
            adj[(x, y)].add((x + dx, y + dy))
        pos = {(x + dx, y + dy) for x, y in pos}
    elif c == "(":
        stack.append((starts, ends))
        starts, ends = pos, set()
    elif c == ")":
        pos.update(ends)
        starts, ends = stack.pop()

seen_with_steps = {(0, 0): 0}
q = deque([((0, 0), 0)])
while q:
    pos, steps = q.popleft()
    for n in adj[pos]:
        if n not in seen_with_steps:
            seen_with_steps[n] = steps + 1
            q.append((n, steps + 1))

print(max(seen_with_steps.values()))
print(sum(1 for v in seen_with_steps.values() if v >= 1000))
