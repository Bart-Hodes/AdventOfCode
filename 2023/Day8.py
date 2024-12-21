from aocd.models import Puzzle


def part_a(data):
    print(data)

    return None


def part_b(data):

    return None


if __name__ == "__main__":
    puzzle = Puzzle(2023, 8)
    examples = puzzle.examples
    for example in examples:
        print(part_a(example.input_data))
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
