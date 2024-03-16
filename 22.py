import heapq
import re
from aoc import DIRS, read_input

lines = read_input()

depth = int(lines[0].split()[1])
tx, ty = [int(n) for n in re.findall("\d+", lines[1])]


def generate_grid(cx, cy):
    grid = [[(0, 0, 0)] * (cx + 1) for _ in range(cy + 1)]

    for y in range(cy + 1):
        for x in range(cx + 1):
            match (x, y):
                case p if p == (0, 0) or p == (tx, ty):
                    geological_index = 0
                case (0, _):
                    geological_index = y * 48271
                case (_, 0):
                    geological_index = x * 16807
                case _:
                    geological_index = grid[y - 1][x][1] * grid[y][x - 1][1]

            erosion = (geological_index + depth) % 20183
            risk = erosion % 3
            grid[y][x] = (geological_index, erosion, risk)

    return grid


p1_grid = generate_grid(tx, ty)
total = 0
for y in range(ty + 1):
    for x in range(tx + 1):
        total += p1_grid[y][x][2]

print(total)

p2_grid = generate_grid(tx + 100, ty + 100)

tools_per_region = {
    0: ["climbing", "torch"],
    1: ["climbing", "neither"],
    2: ["torch", "neither"],
}

queue = [(0, (0, 0), "torch")]
seen = set()
while len(queue) > 0:
    minutes, pos, tool = heapq.heappop(queue)

    if pos == (tx, ty) and tool == "torch":
        print(minutes)
        exit()

    if (pos, tool) in seen:
        continue
    else:
        seen.add((pos, tool))

    available_tools = tools_per_region[p2_grid[pos[1]][pos[0]][2]]
    for available_tool in available_tools:
        if available_tool != tool:
            heapq.heappush(queue, (minutes + 7, pos, available_tool))

    for dx, dy in DIRS:
        nx, ny = pos[0] + dx, pos[1] + dy
        if nx < 0 or nx >= len(p2_grid[0]) or ny < 0 or ny >= len(p2_grid):
            continue

        neighbor_type = p2_grid[ny][nx][2]
        for neighbor_tool in tools_per_region[neighbor_type]:
            if neighbor_tool == tool:
                heapq.heappush(queue, (minutes + 1, (nx, ny), neighbor_tool))
