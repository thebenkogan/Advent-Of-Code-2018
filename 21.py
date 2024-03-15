import re
from aoc import read_input
from device import get_op

lines = read_input()

ip_register = int(lines[0].split()[1])

instructions = []
for inst in lines[1:]:
    op_name = inst.split()[0]
    a, b, c = [int(n) for n in re.findall("\d+", inst)]
    op = get_op(op_name)
    instructions.append((op, a, b, c))

seen = set()


def run(registers):
    ip = 0

    while 0 <= ip < len(instructions):
        registers[ip_register] = ip

        op, a, b, c = instructions[ip]
        op(registers, a, b, c)

        ip = registers[ip_register] + 1

    return registers[0]


# run the program until line 28 executes, check register 3 and register 0 should match that value
registers_p1 = [0] * 6
registers_p1[0] = 6132825
run(registers_p1)
print(6132825)

# run the program and keep track of all register 3 values seen, once we see a repeat, the values will continue repeating
# the value before the first repeat is the register 0 we are looking for
print(8307757)
