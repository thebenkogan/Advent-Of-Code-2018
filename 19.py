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


def run(registers):
    ip = 0

    while 0 <= ip < len(instructions):
        registers[ip_register] = ip

        op, a, b, c = instructions[ip]
        op(registers, a, b, c)

        ip = registers[ip_register] + 1

    return registers[0]


registers_p1 = [0] * 6
print(run(registers_p1))


# part 2 was just simulating the summation of the factors of 10551425

factors = [i for i in range(1, 10551425 + 1) if 10551425 % i == 0]
print(sum(factors))
