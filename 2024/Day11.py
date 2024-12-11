from aocd import data
from aocd.models import Puzzle


def part_a(data):
    data = data.split(" ")
    data = [int(x) for x in data]

    return calcAmountOfStones(data, 25, {})


def calcAmountOfStones(stones, count, cache):
    if count == 0:
        return len(stones)
    result = 0
    for stone in stones:
        if (stone, count) in cache:
            result += cache[(stone, count)]
        else:
            new_stones = TransformStones(stone)
            answer = calcAmountOfStones(new_stones, count - 1, cache)
            cache[(stone, count)] = answer
            result += answer
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


def part_b(data):
    data = data.split(" ")
    data = [int(x) for x in data]

    return calcAmountOfStones(data, 75, {})


if __name__ == "__main__":
    puzzle = Puzzle(2024, 11)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         if int(example.answer_a) != part_a(example.input_data):
    #             print("Example part A failed!")
    #             print(f"Expected: {example.answer_a}")
    #             print(f"Got: {part_a(example.input_data)}")
    # if example.answer_b:
    #     if int(example.answer_b) != part_b(example.input_data):
    #         print("Example part B failed!")
    #         print(f"Expected: {example.answer_b}")
    #         print(f"Got: {part_b(example.input_data)}")
    puzzle.answer_a = part_a(data)
    puzzle.answer_b = part_b(data)
