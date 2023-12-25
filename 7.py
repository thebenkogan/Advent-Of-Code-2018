from collections import defaultdict
from heapq import heapify, heappop, heappush
import re
from aoc import read_input

lines = read_input()

adj = defaultdict(list)
indegree = defaultdict(int)
for line in lines:
    before, after = re.findall(" ([A-Z]) ", line)
    adj[before].append(after)
    adj[after] = adj[after]
    indegree[before] = indegree[before]
    indegree[after] += 1


def part1(adj, indegree):
    indegree_zero = [n for n, v in indegree.items() if v == 0]
    heapify(indegree_zero)

    order = ""
    while len(indegree_zero) > 0:
        node = heappop(indegree_zero)
        order += node
        for n in adj[node]:
            indegree[n] -= 1
            if indegree[n] == 0:
                heappush(indegree_zero, n)

    return order


print(part1(adj, indegree.copy()))

indegree_zero = [n for n, v in indegree.items() if v == 0]
heapify(indegree_zero)
workers = [None for _ in range(5)]
second = 0
while True:
    # decrement times, pushing new tasks onto the queue if completed
    for i, w in enumerate(workers):
        if w != None:
            workers[i] = (w[0], w[1] - 1)
            if workers[i][1] == 0:
                for n in adj[workers[i][0]]:
                    indegree[n] -= 1
                    if indegree[n] == 0:
                        heappush(indegree_zero, n)

    # assign tasks
    for i in range(len(workers)):
        if workers[i] == None or workers[i][1] == 0:
            if len(indegree_zero) == 0:
                workers[i] = None
            else:
                nxt = heappop(indegree_zero)
                workers[i] = (nxt, ord(nxt) - 4)

    if all(w == None for w in workers):
        break

    second += 1

print(second)
