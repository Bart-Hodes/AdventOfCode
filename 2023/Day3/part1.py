import re

with open("2023/Day3/input.txt", "r") as puzzleInput:
    lines = puzzleInput.read().split("\n")

count = 0
adjecent = set()
for row, line in enumerate(lines):
    for symbol in re.finditer(r"[^\d\.\n]", line):
        col = symbol.start()
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                adjecent.add((r, c))

for row, line in enumerate(lines):
    for number in re.finditer(r"\d+", line):
        span = number.span()
        for c in range(*span):
            if (row, c) in adjecent:
                count += int(number.group())
                break

print(count)
