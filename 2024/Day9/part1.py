with open("input.txt") as file:
    fileSystem = file.read().strip()

print(fileSystem)
fileSystem = list(fileSystem)
count = 0
checksum = 0

idx = 0
while idx < len(fileSystem):
    size = fileSystem[idx]
    if idx % 2 == 0:
        for i in range(int(size)):
            checksum += count * (idx // 2)
            count += 1

    else:
        i = 0
        while i < int(size):
            if int(fileSystem[-1]) != 0:
                checksum += len(fileSystem) // 2 * count
                count += 1
                fileSystem[-1] = int(fileSystem[-1]) - 1
                i += 1
            else:
                fileSystem = fileSystem[:-2]
    idx += 1
print(checksum)
