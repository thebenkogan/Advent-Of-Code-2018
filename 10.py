import re
from aoc import read_input

lines = read_input()

points = []
for line in lines:
    x, y, vx, vy = [int(n) for n in re.findall("-?\d+", line)]
    points.append((x, y, vx, vy))

seconds = 0
while True:
    seconds += 1
    min_x, min_y, max_x, max_y = 1e8, 1e8, -1e8, -1e8
    for i, (x, y, vx, vy) in enumerate(points):
        min_x = min(x + vx, min_x)
        max_x = max(x + vx, max_x)
        min_y = min(y + vy, min_y)
        max_y = max(y + vy, max_y)
        points[i] = (x + vx, y + vy, vx, vy)

    if max_x - min_x < 65 and max_y - min_y < 10:
        grid = [["."] * (max_x - min_x + 1) for _ in range(max_y - min_y + 1)]
        for x, y, _, _ in points:
            grid[y - min_y][x - min_x] = "#"

        for row in grid:
            print("".join(row))

        print(seconds)
        break
