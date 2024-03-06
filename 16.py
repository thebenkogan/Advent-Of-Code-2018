from collections import defaultdict
import re
from aoc import read_input
from device import ops

lines = read_input(split_lines=False)

samples, program = lines.split("\n\n\n\n")


sample_counts = defaultdict(set)


total = 0
for sample in samples.split("\n\n"):
    split = sample.split("\n")
    before = [int(n) for n in re.findall("\d+", split[0])]
    op_code, a, b, c = [int(n) for n in re.findall("\d+", split[1])]
    after = [int(n) for n in re.findall("\d+", split[2])]

    behave_like = 0
    for opt in range(16):
        after_opt = before.copy()
        ops[opt](after_opt, a, b, c)
        if after_opt == after:
            behave_like += 1
            sample_counts[op_code].add(opt)

    if behave_like >= 3:
        total += 1

print(total)

code_to_index = {}
while len(sample_counts) > 0:
    op_code, idxs = min(sample_counts.items(), key=lambda c: len(c[1]))
    idx = list(idxs)[0]
    code_to_index[op_code] = idx
    for op in sample_counts.keys():
        if idx in sample_counts[op]:
            sample_counts[op].remove(idx)
    del sample_counts[op_code]

registers = [0] * 4
for instruction in program.split("\n"):
    op_code, a, b, c = [int(n) for n in re.findall("\d+", instruction)]
    ops[code_to_index[op_code]](registers, a, b, c)

print(registers[0])
