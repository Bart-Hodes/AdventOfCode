import re
import math

with open("2023/Day3/input.txt", "r") as puzzleInput:
    lines = puzzleInput.read().split("\n")

count = 0
gears = {}
for row, line in enumerate(lines):
    for symbol in re.finditer(r"\*", line):
        col = symbol.start()
        gears[(row, col)] = []

for row, line in enumerate(lines):
    for num in re.finditer(r"\d+", line):
        for r in range(row - 1, row + 2):
            for c in range(num.start() - 1, num.end() + 1):
                if (r, c) in gears:
                    gears[(r, c)].append(int(num.group()))

for g, nums in gears.items():
    if len(nums) == 2:
        count += math.prod(nums)

print(count)
