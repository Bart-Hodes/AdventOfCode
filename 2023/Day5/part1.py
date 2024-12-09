import re

def x_to_x_Map(seedId, rule):
    if int(rule[1]) <= int(seedId) < int(rule[1]) + int(rule[2]):
        seedId = int(rule[0]) + (int(seedId) - int(rule[1]))
        return seedId, True
    return seedId, False


with open("2023/Day5/input.txt", "r") as puzzleInput:
    lines = puzzleInput.read().split("\n")

lines[-1] += "\n"

seedIds = re.findall(r"\d+", lines[0])
seedIds = [int(seedId) for seedId in seedIds]


# Get sead IDs
Maps = re.findall(r"(?:\d+ \d+ \d+\n)+", "\n".join(lines[1:]), re.MULTILINE)
# print(Maps)
for map in Maps:
    # print(map)
    # print(seedIds)
    for idx, seedId in enumerate(seedIds):
        for rule in map.split("\n"):
            if rule:
                seedIds[idx], Mutable = x_to_x_Map(seedId, rule.split(" "))
                if Mutable:
                    break
print(seedIds)
print(min(seedIds))


