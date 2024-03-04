from aoc import in_bounds, read_input

lines = [[c for c in line] for line in read_input()]

D = [(0, 1), (1, 0), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
inb = in_bounds(len(lines[0]), len(lines))

# An open acre will become filled with trees if three or more adjacent acres contained trees. Otherwise, nothing happens.

# An acre filled with trees will become a lumberyard if three or more adjacent acres were lumberyards. Otherwise, nothing happens.

# An acre containing a lumberyard will remain a lumberyard if it was adjacent to at least one other lumberyard and at least one acre
# containing trees. Otherwise, it becomes open.


def step(lines):
    new_lines = [[c for c in line] for line in lines]
    for i, row in enumerate(lines):
        for j, c in enumerate(row):
            counts = {".": 0, "|": 0, "#": 0}
            for dx, dy in D:
                nx, ny = j + dx, i + dy
                if inb((nx, ny)):
                    counts[lines[ny][nx]] += 1

            match c:
                case "." if counts["|"] >= 3:
                    new_lines[i][j] = "|"
                case "|" if counts["#"] >= 3:
                    new_lines[i][j] = "#"
                case "#" if not (counts["#"] >= 1 and counts["|"] >= 1):
                    new_lines[i][j] = "."

    return new_lines


p1_lines = lines
for _ in range(10):
    p1_lines = step(p1_lines)


counts = {".": 0, "|": 0, "#": 0}
for row in p1_lines:
    for c in row:
        counts[c] += 1

print(counts["|"] * counts["#"])

seen = {}
res = []
i = 0
while True:
    i += 1
    lines = step(lines)

    counts = {".": 0, "|": 0, "#": 0}
    for row in lines:
        for c in row:
            counts[c] += 1

    res.append(counts["|"] * counts["#"])

    hsh = str(lines)
    if hsh in seen:
        cycle_length = i - seen[hsh]
        idx = (1000000000 - i) % cycle_length
        cycle = res[-cycle_length:]
        print(cycle[idx - 1])
        break
    else:
        seen[hsh] = i
