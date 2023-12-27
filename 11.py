from collections import defaultdict
from aoc import read_input

lines = read_input()
serial_number = int(lines[0])

# (x, y, square size) -> power total
sums = defaultdict(int)

for x in range(1, 301):
    for y in range(1, 301):
        rack_id = x + 10
        power_level = rack_id * y
        power_level += serial_number
        power_level *= rack_id
        power_level = (power_level // 100) % 10
        power_level -= 5
        sums[(x - 1, y - 1, 1)] = power_level

max_power = 0
id = (0, 0)
for size in range(2, 301):
    for i in range(300 - size):
        for j in range(300 - size):
            # imagine putting a one smaller square at this position
            # it covers everything except one additional row and column
            # we can place another one smaller square at (j+1,i+1) to catch those
            # then there is a two smaller square at (j+1,i+1) that is double counted, so subtract that
            # finally, add in the corners
            total = (
                sums[(j, i, size - 1)]
                + sums[(j + 1, i + 1, size - 1)]
                - sums[(j + 1, i + 1, size - 2)]
                + sums[(j + size - 1, i, 1)]
                + sums[(j, i + size - 1, 1)]
            )
            if total > max_power:
                max_power = total
                id = (j + 1, i + 1, size)
            sums[(j, i, size)] = total


print(id)
