from aocd.models import Puzzle


def part_a(data):
    schematics = data.split("\n\n")

    keys = []
    locks = []

    for schematic in schematics:
        # Count number of # in each column
        columns = [-1] * len(schematic.splitlines()[0])
        for line in schematic.splitlines():
            for i, char in enumerate(line):
                if char == "#":
                    columns[i] += 1
        if schematic[0][0] == "#":
            locks.append(columns)
        else:
            keys.append(columns)

    # Check which keys and locks fit together
    count = 0
    for key in keys:
        for lock in locks:
            temp = [lock[i] + key[i] for i in range(len(lock))]
            if max(temp) <= 5:
                count += 1
    return count


def part_b(data):
    return ""


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=25)
    puzzle.answer_a = part_a(puzzle.input_data)
