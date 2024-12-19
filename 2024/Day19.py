from functools import cache
from aocd.models import Puzzle


@cache
def composable(string, substrings):
    # If string is empty we have found a valid composition
    if string == "":
        return True

    # Check substrings for valid composition
    for substring in substrings:
        if string.startswith(substring):
            if composable(string[len(substring) :], substrings):
                return True

    return False


@cache
def numberOfPossibleCompositions(string, substrings):
    # If string is empty we have found a valid composition
    if string == "":
        return 1

    total_compositions = 0

    # Check substrings for possible compositions
    for substring in substrings:
        if string.startswith(substring):
            total_compositions += numberOfPossibleCompositions(
                string[len(substring) :], substrings
            )

    return total_compositions


def part_a(data):
    lines = data.split("\n")

    availiblePatterns = set(lines[0].split(", "))

    numPossiblePatterns = 0
    for desiredPattern in lines[2:]:
        if composable(desiredPattern, tuple(availiblePatterns)):
            numPossiblePatterns += 1

    return str(numPossiblePatterns)


def part_b(data):
    lines = data.split("\n")

    availiblePatterns = set(lines[0].split(", "))

    numPossiblePatterns = 0
    for desiredPattern in lines[2:]:

        numPossiblePatterns += numberOfPossibleCompositions(
            desiredPattern, tuple(availiblePatterns)
        )

    return str(numPossiblePatterns)


if __name__ == "__main__":
    puzzle = Puzzle(2024, 19)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
