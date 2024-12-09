# Read the disk map from the input file
with open("2024/Day9/input.txt") as file:
    fileSystem = list(file.read().strip())

fileIDs = [x for x in range(0, (len(fileSystem) + 1) // 2)]


fileIDs.reverse()
mutations = []

for fileID in fileIDs:
    fileSize = int(fileSystem[fileID * 2])

    for spaceIdx in range(1, fileID * 2, 2):
        if int(fileSystem[spaceIdx]) >= fileSize:
            mutations.append((spaceIdx, fileID, fileSize))
            fileSystem[spaceIdx] = int(fileSystem[spaceIdx]) - int(fileSize)
            fileSystem[fileID * 2 - 1] = int(fileSystem[fileID * 2 - 1]) + int(
                fileSystem[fileID * 2]
            )
            fileSystem[fileID * 2] = 0

            break

mutations.sort(key=lambda x: x[0])


checksum = 0
index = 0
for i in range(len(fileSystem)):
    if i % 2 == 0:
        for checksumIdx in range(index, index + int(fileSystem[i]), 1):
            checksum += checksumIdx * i // 2
        index += int(fileSystem[i])

        j = 0
        while mutations and mutations[j][0] - 1 == i:
            for checksumIdx in range(index, index + int(mutations[j][2]), 1):
                checksum += checksumIdx * mutations[j][1]
            index += int(mutations[j][2])
            mutations.pop(j)

    else:
        index += int(fileSystem[i])


print(checksum)
