from aocd.models import Puzzle

import hashlib


def part_a(data):
    number = 1
    while True:
        # Create the string to hash
        input_string = data + str(number)

        # Compute the MD5 hash
        md5_hash = hashlib.md5(input_string.encode()).hexdigest()

        # Check if the hash starts with five zeroes
        if md5_hash.startswith("00000"):
            break

        # Increment the number and try again
        number += 1
    return number


def part_b(data):
    number = 1
    while True:
        # Create the string to hash
        input_string = data + str(number)

        # Compute the MD5 hash
        md5_hash = hashlib.md5(input_string.encode()).hexdigest()

        # Check if the hash starts with five zeroes
        if md5_hash.startswith("000000"):
            break

        # Increment the number and try again
        number += 1
    return number


if __name__ == "__main__":
    puzzle = Puzzle(2015, 4)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
