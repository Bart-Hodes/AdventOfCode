from aocd import data
from aocd.models import Puzzle

import re


def x_to_x_Map(seedId, rule):
    if int(rule[1]) <= int(seedId) < int(rule[1]) + int(rule[2]):
        seedId = int(rule[0]) + (int(seedId) - int(rule[1]))
        return seedId, True
    return seedId, False


def part_a(data):
    lines = data.split("\n")

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
    return min(seedIds)


# def part_b(data):
#     lines = data.split("\n")

#     lines[-1] += "\n"

#     seedRange = re.findall(r"\d+ \d+", lines[0])

#     seedIds = []
#     for indexes in seedRange:
#         begin, end = indexes.split(" ")
#         seedIds.extend([x for x in range(int(begin), int(begin) + int(end))])

#     # Get sead IDs
#     Maps = re.findall(r"(?:\d+ \d+ \d+\n)+", "\n".join(lines[1:]), re.MULTILINE)
#     for map in Maps:
#         for idx, seedId in enumerate(seedIds):
#             for rule in map.split("\n"):
#                 if rule:
#                     seedIds[idx], Mutable = x_to_x_Map(seedId, rule.split(" "))
#                     if Mutable:
#                         break

#     return min(seedIds)


if __name__ == "__main__":
    puzzle = Puzzle(2023, 5)
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
    # puzzle.answer_b = part_b(data)
