from aocd.models import Puzzle
import re
import cmath


def part_a(data: str):

    position = complex(0, 0)
    orientation = complex(1, 0)

    pattern = r"(\b[L|R])(\d+\b)"

    matches = re.finditer(pattern, data)
    for match in matches:
        letter, value = match.groups()
        if letter == "R":
            orientation = orientation * 1j
        if letter == "L":
            orientation = orientation * -1j

        position += orientation * int(value)

    return int(abs(position.real) + abs(position.imag))

def part_b(data: str):

    position = complex(0, 0)
    orientation = complex(1, 0)

    visited_positions = set()
    visited_positions.add(position)


    pattern = r"(\b[L|R])(\d+\b)"

    matches = re.finditer(pattern, data)
    for match in matches:
        letter, value = match.groups()
        if letter == "R":
            orientation = orientation * 1j
        if letter == "L":
            orientation = orientation * -1j

        for __ in range(int(value)):
            position += orientation

            # Check if position has been visted otherwise add to the list
            if position in visited_positions:
                return int(abs(position.real)+ abs(position.imag))
            else:
                visited_positions.add(position)
    return None

if __name__ == "__main__":
    puzzle = Puzzle(2016, 1)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
