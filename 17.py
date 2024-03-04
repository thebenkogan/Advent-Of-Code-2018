from collections import deque
import re
from aoc import read_input

lines = read_input()

clay = set()
min_x, max_x, min_y, max_y = 1e6, 0, 1e6, 0
for line in lines:
    a, b, c = [int(n) for n in re.findall("\d+", line)]
    x, y = (a, b) if line[0] == "x" else (b, a)
    for i in range(b, c + 1):
        if line[0] == "x":
            y = i
        else:
            x = i
        clay.add((x, y))
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        min_y = min(min_y, y)
        max_y = max(max_y, y)

settled = set()
reachable = set()
sources = deque([(500, 0)])
seen = set([(500, 0)])
while len(sources) > 0:
    wx, wy = sources.popleft()

    # move it down until stopped by settled water / clay or hit the max
    while wy <= max_y and (wx, wy) not in clay and (wx, wy) not in settled:
        if wy >= min_y:
            reachable.add((wx, wy))
        wy += 1

    if (wx, wy) not in clay and (wx, wy) not in settled:
        continue
    else:
        # square above the clay we stopped at
        wy -= 1

    # scan left and right for places water can continue flowing
    # new_sources contains new positions that water can continue dropping from
    new_sources = []
    while len(new_sources) == 0:
        right = wx
        while True:
            right += 1
            if (right, wy) in clay:
                break
            if (right, wy + 1) not in clay and (right, wy + 1) not in settled:
                new_sources.append((right, wy))
                break

        left = wx
        while True:
            left -= 1
            if (left, wy) in clay:
                break
            if (left, wy + 1) not in clay and (left, wy + 1) not in settled:
                new_sources.append((left, wy))
                break

        for x in range(left + 1, right):
            reachable.add((x, wy))
            if len(new_sources) == 0:
                settled.add((x, wy))

        wy -= 1

    # add the new sources if we aren't already queued up to drop from there
    # sources can be duplicated if two different sources drop into the same bucket
    for source in new_sources:
        if source not in seen:
            sources.append(source)
            seen.add(source)

print(len(reachable))
print(len(settled))
