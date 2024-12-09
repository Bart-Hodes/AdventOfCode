with open("input.txt", "r") as f:
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
            if antenna1[0] - dx >= 0 and antenna1[1] - dy >= 0 and antenna1[0] - dx < cols and antenna1[1] - dy < rows:
                print(f"Adding antinode at {(antenna1[0] - dx, antenna1[1] - dy)}")
                antiNodes.add((antenna1[0] - dx, antenna1[1] - dy))
            if antenna2[0] + dx >= 0 and antenna2[1] + dy >= 0 and antenna2[0] + dx < cols and antenna2[1] + dy < rows:
                print(f"Adding antinode at {(antenna2[0] + dx, antenna2[1] + dy)}")
                antiNodes.add((antenna2[0] + dx, antenna2[1] + dy))

print(len(antiNodes))
           


