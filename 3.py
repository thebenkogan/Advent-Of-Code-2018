from collections import defaultdict
import re
from aoc import read_input

lines = read_input()

counts = defaultdict(int)
id_to_squares = {}

for line in lines:
    id, x, y, w, h = [int(n) for n in re.findall("\d+", line)]
    squares = []
    for i in range(w):
        for j in range(h):
            dx = x + i
            dy = y + j
            counts[(dx, dy)] += 1
            squares.append((dx, dy))
    id_to_squares[id] = squares

print(sum([1 for v in counts.values() if v >= 2]))

for id, squares in id_to_squares.items():
    if all(counts[s] == 1 for s in squares):
        print(id)
        break
