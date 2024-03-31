import re
from aoc import read_input
from collections import defaultdict

lines = read_input()


def dist(p1, p2):
    return (
        abs(p1[0] - p2[0])
        + abs(p1[1] - p2[1])
        + abs(p1[2] - p2[2])
        + abs(p1[3] - p2[3])
    )


points = []
for line in lines:
    a, b, c, d = [int(n) for n in re.findall("-?\d+", line)]
    points.append((a, b, c, d))

adj = defaultdict(list)
for point in points:
    for other in points:
        if point != other and dist(point, other) <= 3:
            adj[point].append(other)


total = 0
seen = set()
for point in points:
    if point in seen:
        continue
    else:
        seen.add(point)

    total += 1

    stack = [point]
    while len(stack) > 0:
        p = stack.pop()
        for n in adj[p]:
            if n not in seen:
                seen.add(n)
                stack.append(n)

print(total)
