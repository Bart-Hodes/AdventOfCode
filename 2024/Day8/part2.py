with open("2024/Day8/input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

antennaDict = {}
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != ".":
            if char not in antennaDict:
                antennaDict[char] = []
            antennaDict[char].append((x, y))

rows = len(lines)
cols = len(lines[0])

antiNodes = set()

for frequency in antennaDict:
    print(f"{frequency}: {antennaDict[frequency]}")
    for idx, antenna1 in enumerate(antennaDict[frequency]):
        for antenna2 in antennaDict[frequency][idx+1:]:
            print(f"Checking {antenna1} and {antenna2}")
            dx = antenna2[0] - antenna1[0]
            dy = antenna2[1] - antenna1[1]

            if len(antennaDict[frequency]) >2:
                antiNodes.add(antenna1)
                antiNodes.add(antenna2)
            while antenna1[0] - dx >= 0 and antenna1[1] - dy >= 0 and antenna1[0] - dx < cols and antenna1[1] - dy < rows:
                print(f"Adding antinode at {(antenna1[0] - dx, antenna1[1] - dy)}")
                antiNodes.add((antenna1[0] - dx, antenna1[1] - dy))
                dx += antenna2[0] - antenna1[0]
                dy += antenna2[1] - antenna1[1]

            dx = antenna2[0] - antenna1[0]
            dy = antenna2[1] - antenna1[1]
            while antenna2[0] + dx >= 0 and antenna2[1] + dy >= 0 and antenna2[0] + dx < cols and antenna2[1] + dy < rows:
                print(f"Adding antinode at {(antenna2[0] + dx, antenna2[1] + dy)}")
                antiNodes.add((antenna2[0] + dx, antenna2[1] + dy))
                dx += antenna2[0] - antenna1[0]
                dy += antenna2[1] - antenna1[1]
                

# print lines with antenna nodes
for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char != ".":
            print(char, end="")
        elif (x, y) in antiNodes:
            print("#", end="")
        else:
            print(char, end="")
    print()

print(len(antiNodes))
           


