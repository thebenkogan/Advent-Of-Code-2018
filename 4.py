from collections import defaultdict
import re
from aoc import read_input

lines = read_input()

records = []
for line in lines:
    d = line[1:].split("]")[0]
    if "Guard" in line:
        num = int(re.findall("#(\d+)", line)[0])
        records.append((d, num))
    elif "falls" in line:
        records.append((d, "f"))
    else:
        records.append((d, "w"))

records = sorted(records)

counts = defaultdict(lambda: defaultdict(int))

i = 0
while i < len(records):
    _, guard = records[i]

    i += 1
    while i < len(records) and records[i][1] == "f":
        start_min = int(re.findall(":(\d+)", records[i][0])[0])
        end_min = int(re.findall(":(\d+)", records[i + 1][0])[0])
        for min in range(start_min, end_min):
            counts[guard][min] += 1
        i += 2

max_mins = 0
id = 0
most_min = 0
for guard, min_sleeps in counts.items():
    total = sum(min_sleeps.values())
    if total > max_mins:
        max_mins = total
        id = guard
        most_min = max(min_sleeps.items(), key=lambda m: m[1])[0]

print(id * most_min)

freq = 0
id = 0
most_min = 0
for guard, min_sleeps in counts.items():
    min, min_freq = max(min_sleeps.items(), key=lambda m: m[1])
    if min_freq > freq:
        freq = min_freq
        id = guard
        most_min = min

print(id * most_min)
