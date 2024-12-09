# Read the disk map from the input file
with open("test.txt") as file:
    fileSystem = file.read().strip()

# Decompress the dense format to represent the disk
decompressedMemory = []
i = 0
while i < len(fileSystem):
    if i % 2 == 0:  # File length
        file_id = str(i // 2)  # File ID
        file_length = int(fileSystem[i])
        decompressedMemory.extend([file_id] * file_length)
    else:  # Free space length
        free_space_length = int(fileSystem[i])
        decompressedMemory.extend(["."] * free_space_length)
    i += 1


# Start compacting files by moving them whole in reverse order of their IDs
file_ids = sorted(set(c for c in decompressedMemory if c != "."), reverse=True)

for currentFileID in file_ids:
    # Find the current blocks occupied by the file start with the last one
    file_blocks = [i for i, c in enumerate(decompressedMemory) if c == currentFileID]

    # Determine the file size
    file_size = len(file_blocks)

    # Find the leftmost free span large enough for the file
    free_space_start = None
    current_free_span = 0
    for i, block in enumerate(decompressedMemory[: file_blocks[0] + 1]):
        if block == ".":
            if current_free_span == 0:
                free_space_start = i
            current_free_span += 1
            if current_free_span == file_size:
                break
        else:
            current_free_span = 0

    # If no suitable free space found, skip moving this file
    if current_free_span < file_size:
        continue

    # Clear the current file blocks
    for idx in file_blocks:
        decompressedMemory[idx] = "."

    # Move the file to the free space
    for i in range(file_size):
        decompressedMemory[free_space_start + i] = currentFileID

    # strip the trailing dots
    while decompressedMemory[-1] == ".":
        decompressedMemory = decompressedMemory[:-1]


# Calculate the checksum
checksum = 0
for idx, fileID in enumerate(decompressedMemory):
    if fileID != ".":
        checksum += idx * int(fileID)

# Print the resulting checksum
print(checksum)
