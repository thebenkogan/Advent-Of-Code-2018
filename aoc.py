import sys


def read_input(split_lines=True):
    day = sys.argv[0].split(".")[0]
    is_test = "test" in sys.argv[1:]
    name = "test" if is_test else "in"
    with open(f"data/{day}/{name}.txt") as f:
        if split_lines:
            return f.read().splitlines()
        return f.read()


DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def in_bounds(a, b):
    return lambda c: 0 <= c[0] < a and 0 <= c[1] < b


# queue = deque()
# seen = set()

# while len(queue) > 0:
#     elt = queue.popleft()
#     for n in neighbors:
#         if n not in seen:
#             seen.add(n)
#             queue.append(n)
