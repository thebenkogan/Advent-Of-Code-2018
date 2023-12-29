from collections import deque
from aoc import read_input

lines = read_input()

adj = {}
units = {}

for y, row in enumerate(lines):
    for x, c in enumerate(row):
        if c != "#":
            neighbors = []
            for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                nx, ny = x + dx, y + dy
                if lines[ny][nx] != "#":
                    neighbors.append((nx, ny))
            adj[(x, y)] = neighbors

        if c == "E":
            units[(x, y)] = ("E", 200)

        if c == "G":
            units[(x, y)] = ("G", 200)


def next_step(units, unit_pos):
    unit_type = units[unit_pos][0]

    # target position -> (next position, minimum distance) or None if not reachable
    targets = {}
    for pos, (t, _) in units.items():
        if t != unit_type:
            for n in [n for n in adj[pos] if n not in units]:
                targets[n] = None

    if len(targets) == 0:
        return None

    queue = deque([([], 0, unit_pos)])
    seen = set([unit_pos])
    while queue:
        path, steps, pos = queue.popleft()
        if pos in targets and targets[pos] == None:
            targets[pos] = (path[0], steps)
        for n in adj[pos]:
            if n not in seen and n not in units:
                seen.add(n)
                new_path = path.copy()
                new_path.append(n)
                queue.append((new_path, steps + 1, n))

    next_pos = None
    min_dist = 1e6
    for target in sorted(targets.keys(), key=lambda c: (c[1], c[0])):
        if targets[target] == None:
            continue
        step, dist = targets[target]
        if dist < min_dist:
            min_dist = dist
            next_pos = step
    return next_pos


# returns (updated unit positions, true if combat ended, true if no_dead_elf and elf just died)
def do_round(units, unit_powers, no_dead_elf):
    positions = sorted(units.keys(), key=lambda c: (c[1], c[0]))
    for pos in positions:
        # this unit might have been killed by someone before
        if pos not in units:
            continue

        type, _ = units[pos]

        # check if no enemies exist, in which case combat ends
        if all(t == type for (t, _) in units.values()):
            return units, True, False

        adjacent_enemies = [n for n in adj[pos] if n in units and units[n][0] != type]

        # if no one in range, move first
        if len(adjacent_enemies) == 0:
            next_pos = next_step(units, pos)
            if next_pos != None:
                units[next_pos] = units[pos]
                del units[pos]
                adjacent_enemies = [
                    n for n in adj[next_pos] if n in units and units[n][0] != type
                ]

        # if enemies now in range, attack
        if len(adjacent_enemies) > 0:
            selected = min(
                adjacent_enemies,
                key=lambda c: units[c][1],
            )
            selected_type, selected_hp = units[selected]
            next_hp = selected_hp - unit_powers[type]
            if next_hp <= 0:
                del units[selected]
                if no_dead_elf and selected_type == "E":
                    return units, False, True
            else:
                units[selected] = (selected_type, next_hp)

    return units, False, False


def run_til_combat_ends(units, powers, no_dead_elf):
    rounds = 0
    while True:
        units, ended, elf_died = do_round(units, powers, no_dead_elf)
        if elf_died and no_dead_elf:
            return None
        if ended:
            total_hp = sum(hp for (_, hp) in units.values())
            return total_hp * rounds
        rounds += 1


print(run_til_combat_ends(units.copy(), {"E": 3, "G": 3}, False))

elf_power = 4
while True:
    res = run_til_combat_ends(units.copy(), {"E": elf_power, "G": 3}, True)
    if res != None:
        print(res)
        break
    else:
        elf_power += 1
