from aoc import read_input

lines = read_input()
serial_number = int(lines[0])

grid = [[0] * 300 for _ in range(300)]

for x in range(1, 301):
    for y in range(1, 301):
        rack_id = x + 10
        power_level = rack_id * y
        power_level += serial_number
        power_level *= rack_id
        power_level = (power_level // 100) % 10
        power_level -= 5
        grid[y - 1][x - 1] = power_level

# summed area table (I)
# https://en.wikipedia.org/wiki/Summed-area_table
sums = [[0] * 300 for _ in range(300)]
for i in range(300):
    for j in range(300):
        total = grid[i][j]
        if i > 0 and j > 0:
            total += sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1]
        elif i > 0:
            total += sums[i - 1][j]
        elif j > 0:
            total += sums[i][j - 1]
        sums[i][j] = total

max_power = 0
id = (0, 0, 0)
for size in range(1, 300):
    for i in range(300 - size):
        for j in range(300 - size):
            total = sums[i + size][j + size]
            if i > 0 and j > 0:
                total += (
                    sums[i - 1][j - 1] - sums[i + size][j - 1] - sums[i - 1][j + size]
                )
            elif j > 0:
                total -= sums[i + size][j - 1]
            elif i > 0:
                total -= sums[i - 1][j + size]

            if total > max_power:
                max_power = total
                id = (j + 1, i + 1, size + 1)


print(id)
