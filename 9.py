import re
from aoc import read_input

lines = read_input(split_lines=False)

num_players, last_marble = [int(n) for n in re.findall("\d+", lines)]
last_marble *= 100


class CircleNode:
    def __init__(self, val):
        self.val = val
        self.prev = self
        self.next = self

    def insert_1_after(self, val):
        to_add = CircleNode(val)
        curr = self.next
        after = curr.next

        curr.next = to_add
        after.prev = to_add
        to_add.prev = curr
        to_add.next = after

        return to_add

    def remove_7_before(self):
        curr = self
        for _ in range(7):
            curr = curr.prev

        before = curr.prev
        after = curr.next
        before.next = after
        after.prev = before

        return after, curr.val


players = [0 for _ in range(num_players)]
curr_marble = CircleNode(0)
curr_player = 0

for nxt in range(1, last_marble + 1):
    if nxt == last_marble / 100:
        print(max(players))

    if nxt % 23 == 0:
        curr_marble, removed = curr_marble.remove_7_before()
        players[curr_player] += nxt + removed
    else:
        curr_marble = curr_marble.insert_1_after(nxt)

    curr_player = (curr_player + 1) % num_players

print(max(players))
