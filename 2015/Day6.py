from aocd import data
from aocd.models import Puzzle

import re


def part_a(data):
    data = data.split("\n")

    grid = [[0 for i in range(1000)] for j in range(1000)]

    for instruction in data:
        if instruction.startswith("turn on"):
            instruction = instruction[8:]
            instruction = instruction.replace(" through ", ",")
            instruction = instruction.split(",")
            x1, y1, x2, y2 = map(int, instruction)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    grid[i][j] = 1
        elif instruction.startswith("turn off"):
            instruction = instruction[9:]
            instruction = instruction.replace(" through ", ",")
            instruction = instruction.split(",")
            x1, y1, x2, y2 = map(int, instruction)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    grid[i][j] = 0
        elif instruction.startswith("toggle"):
            instruction = instruction[7:]
            instruction = instruction.replace(" through ", ",")
            instruction = instruction.split(",")
            x1, y1, x2, y2 = map(int, instruction)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    grid[i][j] = 1 - grid[i][j]

    return sum([sum(row) for row in grid])


def part_b(data):
    data = data.split("\n")

    grid = [[0 for i in range(1000)] for j in range(1000)]

    for instruction in data:
        if instruction.startswith("turn on"):
            instruction = instruction[8:]
            instruction = instruction.replace(" through ", ",")
            instruction = instruction.split(",")
            x1, y1, x2, y2 = map(int, instruction)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    grid[i][j] = grid[i][j] + 1
        elif instruction.startswith("turn off"):
            instruction = instruction[9:]
            instruction = instruction.replace(" through ", ",")
            instruction = instruction.split(",")
            x1, y1, x2, y2 = map(int, instruction)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    grid[i][j] = max(0, grid[i][j] - 1)
        elif instruction.startswith("toggle"):
            instruction = instruction[7:]
            instruction = instruction.replace(" through ", ",")
            instruction = instruction.split(",")
            x1, y1, x2, y2 = map(int, instruction)
            for i in range(x1, x2 + 1):
                for j in range(y1, y2 + 1):
                    grid[i][j] = grid[i][j] + 2

    return sum([sum(row) for row in grid])


if __name__ == "__main__":
    puzzle = Puzzle(2015, 6)
    for example in puzzle.examples:
        if example.answer_a:
            if int(example.answer_a) != part_a(example.input_data):
                print("Example part A failed!")
                print(f"Expected: {example.answer_a}")
                print(f"Got: {part_a(example.input_data)}")
                exit()
        if example.answer_b:
            if int(example.answer_b) != part_b(example.input_data):
                print("Example part B failed!")
                print(f"Expected: {example.answer_b}")
                print(f"Got: {part_b(example.input_data)}")

    puzzle.answer_a = part_a(data)
    puzzle.answer_b = part_b(data)
