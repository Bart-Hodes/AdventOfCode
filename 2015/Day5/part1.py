import re

with open("2015/Day5/input.txt") as f:
    data = [line.strip("\n") for line in f.readlines()]


niceCounter = 0
for string in data:
    match = re.findall("[aeiou]", string)
    if len(match) < 3:
        continue
    match = re.findall(r"(.)\1", string)
    if not match:
        continue
    match = re.findall(r"(ab|cd|pq|xy)", string)
    if match:
        continue
    print("Found nice string:", string)
    niceCounter += 1
print("found", niceCounter, "nice strings")