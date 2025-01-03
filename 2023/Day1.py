from aocd.models import Puzzle

import re


mapping = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


# This function will be used to process the matched word and return the corresponding numerical value
def convert_word_to_digit(match):

    word = match.group(1).lower()  # Get matched word, convert to lowercase

    return str(
        mapping.get(word, word)
    )  # Return the digit if in mapping, else the word itself


def part_a(data):
    lines = data.split("\n")

    total = 0
    for line in lines:
        # Match first digit
        first_digit_match = re.search(r"\d", line)
        first_digit = first_digit_match.group(0) if first_digit_match else None

        # Match last digit
        last_digit_match = re.search(r"\d(?=[^\d]*$)", line)
        last_digit = last_digit_match.group(0) if last_digit_match else None

        total += int(first_digit + last_digit)

    return total


def part_b(data):
    lines = data.split("\n")

    total = 0
    for line in lines:
        pattern = r"|".join([re.escape(word) for word in mapping.keys()])
        # Replace all written numbers with their numerical value
        line = re.sub(
            "(?=(one|two|three|four|five|six|seven|eight|nine))",
            convert_word_to_digit,
            line,
            flags=re.IGNORECASE,
        )

        # Match first digit
        first_digit_match = re.search(r"\d", line)
        first_digit = first_digit_match.group(0) if first_digit_match else None

        # Match last digit
        last_digit_match = re.search(r"\d(?=[^\d]*$)", line)
        last_digit = last_digit_match.group(0) if last_digit_match else None

        total += int(first_digit + last_digit)
    return total


if __name__ == "__main__":
    puzzle = Puzzle(2023, 1)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
