from aoc import read_input

lines = read_input()

adj = {}
carts = {}  # position -> direction + intersection turn status
for y, row in enumerate(lines):
    for x, c in enumerate(row):
        if c != " ":
            if c == "-" or c == "<" or c == ">":
                neighbor = lambda dr: (1, 0) if dr[0] == 1 else (-1, 0)
                if c == "<":
                    carts[(x, y)] = (-1, 0, 0)
                if c == ">":
                    carts[(x, y)] = (1, 0, 0)

            if c == "|" or c == "v" or c == "^":
                neighbor = lambda dr: (0, 1) if dr[1] == 1 else (0, -1)
                if c == "v":
                    carts[(x, y)] = (0, 1, 0)
                if c == "^":
                    carts[(x, y)] = (0, -1, 0)

            if c == "/":
                neighbor = lambda dr: (-dr[1], -dr[0])

            if c == "\\":
                neighbor = lambda dr: (dr[1], dr[0])

            if c == "+":
                neighbor = (
                    lambda dr: (-dr[1], -dr[0])
                    if (dr[2] == 0 and dr[1] == 0 or dr[2] == 2 and dr[0] == 0)
                    else (dr[0], dr[1])
                    if dr[2] == 1
                    else (dr[1], dr[0])
                )

            adj[(x, y)] = neighbor

p1_ans = None


def tick(carts):
    global p1_ans
    cart_positions = sorted(carts.keys(), key=lambda c: (c[1], c[0]))
    new_carts = {}

    for pos in cart_positions:
        if pos not in carts:
            continue

        state = carts[pos]
        dx, dy = adj[pos](state)

        next_turn = state[2]
        if lines[pos[1]][pos[0]] == "+":
            next_turn = (next_turn + 1) % 3

        next_pos = (pos[0] + dx, pos[1] + dy)
        if next_pos in carts or next_pos in new_carts:
            if p1_ans == None:
                p1_ans = next_pos
            if next_pos in carts:
                del carts[next_pos]
            if next_pos in new_carts:
                del new_carts[next_pos]
        else:
            new_carts[next_pos] = (dx, dy, next_turn)

        del carts[pos]

    return new_carts


while True:
    carts = tick(carts)
    if len(carts) == 1:
        print(p1_ans)
        print(list(carts.keys())[0])
        break
