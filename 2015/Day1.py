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
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
