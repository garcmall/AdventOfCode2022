
f = open("AoC2022D1 Input")

file = f.read()

elves = file.split("\n\n")
cals = []
for elf in elves:
    elf = elf.split("\n")
    total = 0
    for num in elf:
        num = int(num)
        total += num
    cals.append(total)

#Part 1 solution
print(max(cals))

#Part 2 solution
cals.sort(reverse=True)
print(sum(cals[:3]))
