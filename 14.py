from aoc import read_input

lines = read_input()
num_recipes = int(lines[0])
num_recipes_digits = [int(n) for n in str(num_recipes)]

recipes = [3, 7]
elf1 = 0
elf2 = 1

while True:
    new_recipes = [int(c) for c in str(recipes[elf1] + recipes[elf2])]
    recipes += new_recipes
    elf1 = (elf1 + recipes[elf1] + 1) % len(recipes)
    elf2 = (elf2 + recipes[elf2] + 1) % len(recipes)

    if len(recipes) == num_recipes + 10:
        print("".join(str(n) for n in recipes[-10:]))

    if len(recipes) > len(num_recipes_digits) + 1:
        window = recipes[-len(num_recipes_digits) - 1 :]
        if num_recipes_digits == window[:-1] or num_recipes_digits == window[1:]:
            offset = 1 if num_recipes_digits == window[:-1] else 0
            print(len(recipes) - len(num_recipes_digits) - offset)
            break
