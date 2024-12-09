# You must evaluate a whole block of split if on border

import re

def x_to_x_Map(seedId, rule):
    if int(rule[1]) <= int(seedId) < int(rule[1]) + int(rule[2]):
        seedId = int(rule[0]) + (int(seedId) - int(rule[1]))
        return seedId, True
    return seedId, False


with open("2023/Day5/input.txt", "r") as puzzleInput:
    lines = puzzleInput.read().split("\n")

lines[-1] += "\n"

seedRange = re.findall(r"\d+ \d+", lines[0])

seedIds = []
for indexes in seedRange:
    begin, end = indexes.split(" ")
    seedIds.extend([x for x in range(int(begin),int(begin)+ int(end))])

# Get sead IDs
Maps = re.findall(r"(?:\d+ \d+ \d+\n)+", "\n".join(lines[1:]), re.MULTILINE)
for map in Maps:
    for idx, seedId in enumerate(seedIds):
        for rule in map.split("\n"):
            if rule:
                seedIds[idx], Mutable = x_to_x_Map(seedId, rule.split(" "))
                if Mutable:
                    break

print(min(seedIds))


