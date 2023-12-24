from aoc import read_input

lines = read_input()

res = 0
seen = set([0])
p1_total = 0
while True:
    for line in lines:
        sign = line[0]
        num = int(line[1:])
        if sign == "+":
            res += num
        else:
            res -= num

        if res in seen:
            print(res)
            exit()
        else:
            seen.add(res)

    if p1_total == 0:
        p1_total = res
        print(res)
