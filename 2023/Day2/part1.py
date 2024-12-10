import re

f = open("2023/Day2/input.txt", "r")
# f = open("test.txt","r")

maxRed = 12
maxGreen = 13
maxBlue = 14

count = 0

for line in f:
    # Remove line header
    gameInfo = line.split(":")
    subset = gameInfo[1].split(";")

    # Initial assumption game valid
    valid = True

    minRed = 0
    minGreen = 0
    minBlue = 0
    for game in subset:
        match = re.search("((\d*) red)", game)
        if match != None:
            numRed = int(match.group(2))
        else:
            numRed = 0
        match = re.search("((\d*) blue)", game)
        if match != None:
            numBlue = int(match.group(2))
        else:
            numBlue = 0
        match = re.search("((\d*) green)", game)
        if match != None:
            numGreen = int(match.group(2))
        else:
            numGreen = 0

        # Check game validity
        if not (numRed <= maxRed and numBlue <= maxBlue and numGreen <= maxGreen):
            valid = False

    if valid:
        gameIdx = re.search("(Game (\d*))", gameInfo[0]).group(2)
        count += int(gameIdx)

print(count)
