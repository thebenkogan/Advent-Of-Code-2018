from collections import Counter
from aoc import read_input

lines = read_input()

two = 0
three = 0
for line in lines:
    c = Counter(line)
    vs = c.values()
    if 2 in vs:
        two += 1
    if 3 in vs:
        three += 1

print(two * three)

for i, line in enumerate(lines):
    for j in range(i + 1, len(lines)):
        same = [c1 for (c1, c2) in zip(line, lines[j]) if c1 == c2]
        if len(same) == len(line) - 1:
            print("".join(same))
            exit()
