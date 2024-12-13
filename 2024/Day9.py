from aocd import data
from aocd.models import Puzzle


def part_a(data):
    fileSystem = list(data)
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
    return checksum


def part_b(data):
    fileSystem = list(data)

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
    return checksum


if __name__ == "__main__":
    puzzle = Puzzle(2024, 9)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         if int(example.answer_a) != part_a(example.input_data):
    #             print("Example part A failed!")
    #             print(f"Expected: {example.answer_a}")
    #             print(f"Got: {part_a(example.input_data)}")
    # if example.answer_b:
    #     if int(example.answer_b) != part_b(example.input_data):
    #         print("Example part B failed!")
    #         print(example)
    #         print(f"Expected: {example.answer_b}")
    #         print(f"Got: {part_b(example.input_data)}")
    puzzle.answer_a = part_a(data)
    puzzle.answer_b = part_b(data)
