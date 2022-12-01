
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

cals.sort(reverse=True)

print(sum(cals[:3]))