from collections import defaultdict
from aoc import read_input

lines = read_input()

coords = []
for line in lines:
    x, y = [int(n) for n in line.split(", ")]
    coords.append((x, y))

MIN = 0
MAX = 400

counts = defaultdict(int)
for x in range(MIN, MAX):
    for y in range(MIN, MAX):
        closest = sorted([(abs(c[0] - x) + abs(c[1] - y), c) for c in coords])
        if closest[0][0] != closest[1][0]:
            counts[closest[0][1]] += 1

for i in range(MIN, MAX):
    for x, y in [(i, MAX), (i, MIN), (MIN, i), (MAX, i)]:
        closest = min(coords, key=lambda c: abs(c[0] - x) + abs(c[1] - y))
        if closest in counts:
            del counts[closest]

print(max(counts.values()))

safe = 0
for x in range(MIN, MAX):
    for y in range(MIN, MAX):
        total = sum([abs(c[0] - x) + abs(c[1] - y) for c in coords])
        if total < 10000:
            safe += 1

print(safe)
