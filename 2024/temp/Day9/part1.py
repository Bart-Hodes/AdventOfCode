with open("2024/Day9/input.txt") as file:
    fileSystem = file.read().strip()

decompressedMemory = []

# Build decompressedMemory
i = 0
while i < len(fileSystem):
    if i % 2 == 0:
        for _ in range(int(fileSystem[i])):
            decompressedMemory.append(str(i // 2))
    else:
        decompressedMemory += "." * int(fileSystem[i])
    i += 1


# Modify decompressedMemory by replacing dots
decompressedMemory = list(decompressedMemory)  # Convert string to a list for mutability
i = 0
while i < len(decompressedMemory):
    if decompressedMemory[i] == ".":
        if decompressedMemory[-1] != ".":
            decompressedMemory[i] = decompressedMemory[-1]
            decompressedMemory = decompressedMemory[:-1]  # Trim the last character
        if decompressedMemory[i] == ".":
            decompressedMemory = decompressedMemory[:-1]  # Trim the last character
            continue
    i += 1


# calculate Checksum
checksum = 0
for idx, fileID in enumerate(decompressedMemory):
    checksum += idx * int(fileID)

print(checksum)
