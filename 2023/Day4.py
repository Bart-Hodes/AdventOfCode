from aocd import data
from aocd.models import Puzzle

import re


def part_a(data):
    lines = data.split("\n")

    pattern = r"Card\s+\d+:\s([\d\s]+)\|\s([\d\s]+)"

    count = 0
    for line in lines:
        match = re.search(pattern, line)

        left_numbers = set(match.group(1).split())
        right_numbers = set(match.group(2).split())

        subcount = 0
        for num in left_numbers:
            if num in right_numbers:
                subcount += 1
        if subcount > 0:
            count += 2 ** (subcount - 1)

    return count


def part_b(data):
    lines = data.split("\n")

    pattern = r"Card\s+\d+:\s([\d\s]+)\|\s([\d\s]+)"

    cards = []
    for line in lines:
        match = re.search(pattern, line)

        left_numbers = set(match.group(1).split())
        right_numbers = set(match.group(2).split())

        cards.append([left_numbers, right_numbers])

    card_copies = [1] * len(cards)

    for idx, card in enumerate(cards):
        subcount = 1
        for num in card[0]:
            if num in card[1]:
                card_copies[idx + subcount] += card_copies[idx]
                subcount += 1
    return sum(card_copies)


if __name__ == "__main__":
    puzzle = Puzzle(2023, 4)
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