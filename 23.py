import re
from aoc import read_input

lines = read_input()

bots = []

for line in lines:
    x, y, z, r = [int(n) for n in re.findall("-?\d+", line)]
    bots.append({"pos": (x, y, z), "r": r})

max_bot = max(bots, key=lambda b: b["r"])


def dist(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])


total = 0
for bot in bots:
    d = dist(bot["pos"], max_bot["pos"])
    if d <= max_bot["r"]:
        total += 1

print(total)


bounds = []
for bot in bots:
    d = dist(bot["pos"], (0, 0, 0))
    r = bot["r"]
    left = max(d - r, 0)
    right = d + r + 1
    bounds.append((left, 1))
    bounds.append((right, -1))

bounds = sorted(bounds, key=lambda c: c[0])

best = 0
max_count = 0
count = 0
for d, o in bounds:
    count += o
    if count > max_count:
        max_count = count
        best = d

# approximate
print(best)
