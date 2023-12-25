from aoc import read_input

polymer = read_input(split_lines=False)

cache = {}


def react_once(p, start):
    for i in range(start, len(p) - 1):
        if p[i] != p[i + 1] and p[i].lower() == p[i + 1].lower():
            return p[:i] + p[i + 2 :], max(0, i - 1)
    return None


def full_react(p):
    start = 0
    while True:
        nxt = react_once(p, start)
        if nxt == None:
            return p
        else:
            p = nxt[0]
            start = nxt[1]


print(len(full_react(polymer)))

best = len(polymer)
for type in "abcdefghijklmnopqrstuvwxyz":
    removed = "".join(c for c in polymer if c.lower() != type)
    done = full_react(removed)
    best = min(best, len(done))

print(best)
