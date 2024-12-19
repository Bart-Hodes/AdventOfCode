from functools import cache
from aocd.models import Puzzle


@cache
def calcAmountOfStones(stone, count):
    if count == 0:
        return 1

    result = 0
    for new_stone in TransformStones(stone):
        result += calcAmountOfStones(new_stone, count - 1)

    return result


def TransformStones(stone):
    result = []
    if stone == 0:
        result.append(1)
    elif len(str(stone)) % 2 == 0:
        mid = len(str(stone)) // 2
        result.append(int(str(stone)[mid:]))
        result.append(int(str(stone)[:mid]))
    else:
        result.append(stone * 2024)
    return result


def part_a(data):
    data = [int(x) for x in data.split(" ")]
    return str(sum(calcAmountOfStones(stone, 25) for stone in data))


def part_b(data):
    data = [int(x) for x in data.split(" ")]
    return str(sum(calcAmountOfStones(stone, 75) for stone in data))


if __name__ == "__main__":
    puzzle = Puzzle(2024, 11)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
