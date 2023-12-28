from aoc import read_input

lines = read_input(split_lines=False)
sections = lines.split("\n\n")

plants = set()
for i, c in enumerate(sections[0].split(": ")[1]):
    if c == "#":
        plants.add(i)

patterns = {}
for line in sections[1].split("\n"):
    pat, out = line.split(" => ")
    patterns[pat] = out


def gen(plants):
    next_plants = set()

    min_x = min(plants)
    max_x = max(plants)
    for i in range(min_x - 2, max_x + 3):
        pat = ""
        for j in range(5):
            if (i - 2 + j) in plants:
                pat += "#"
            else:
                pat += "."
        if pat in patterns and patterns[pat] == "#":
            next_plants.add(i)

    return next_plants


for _ in range(20):
    plants = gen(plants)

print(sum(plants))

# by observation, each generation adds a variable amount of plants
# up until some point where it hits a steady state. find this point,
# then just multiply to get the answer


totals = [sum(plants)]
generations = 20
while True:
    generations += 1
    plants = gen(plants)
    totals.append(sum(plants))

    # check if last 5 totals have equal deltas
    if len(totals) > 5:
        diff = totals[-1] - totals[-2]
        if all(
            totals[i + 1] - totals[i] == diff
            for i in range(len(totals) - 5, len(totals) - 1)
        ):
            break

diff = totals[-1] - totals[-2]
print(totals[-1] + (50000000000 - generations) * diff)
