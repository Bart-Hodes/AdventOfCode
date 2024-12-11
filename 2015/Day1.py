from aocd import data
from aocd.models import Puzzle


def part_a(data):

    count = 0
    for char in data:

        if char == "(":
            count += 1
        elif char == ")":
            count -= 1

    return count


def part_b(data):
    count = 0
    for idx, char in enumerate(data):
        if char == "(":
            count += 1
        elif char == ")":
            count -= 1
        if count < 0:
            break
    return idx + 1


if __name__ == "__main__":
    puzzle = Puzzle(2015, 1)
    for example in puzzle.examples:
        if example.answer_a:
            if int(example.answer_a) != part_a(example.input_data):
                print("Example part A failed!")
                print(f"Expected: {example.answer_a}")
                print(f"Got: {part_a(example.input_data)}")
        if example.answer_b:
            if int(example.answer_b) != part_b(example.input_data):
                print("Example part B failed!")
                print(f"Expected: {example.answer_b}")
                print(f"Got: {part_b(example.input_data)}")

    puzzle.answer_a = part_a(data)
    puzzle.answer_b = part_b(data)
