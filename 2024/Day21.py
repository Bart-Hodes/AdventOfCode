from aocd.models import Puzzle

from functools import cache

GAP = "."
keypad_numeric = ["789", "456", "123", ".0A"]
keypad_directional = [".^A", "<v>"]


def findPosition(keypad, key):
    for r, row in enumerate(keypad):
        for c, col in enumerate(row):
            if col == key:
                return r, c
    assert False, f"Key {key} not found in keypad"


def findShortestPath(keypad, key1, key2):
    r1, c1 = findPosition(keypad, key1)
    r2, c2 = findPosition(keypad, key2)
    rGap, cGap = findPosition(keypad, GAP)

    dr, dc = r2 - r1, c2 - c1

    if dr == 0 and dc == 0:
        return [""]

    row_moves = "v" * abs(dr) if dr >= 0 else "^" * abs(dr)
    col_moves = ">" * abs(dc) if dc >= 0 else "<" * abs(dc)

    if dr == 0:
        return [col_moves]
    elif dc == 0:
        return [row_moves]
    elif (r1, c2) == (rGap, cGap):
        return [row_moves + col_moves]
    elif (r2, c1) == (rGap, cGap):
        return [col_moves + row_moves]
    else:
        return [row_moves + col_moves, col_moves + row_moves]


def buildSequence(seq, keypad):
    transSeq = []
    for key1, key2 in zip("A" + seq, seq):
        transSeq += [[sp + "A" for sp in findShortestPath(keypad, key1, key2)]]
    return transSeq


@cache
def solveSequence(seq, depth):
    if depth == 0:
        return len(seq)

    if any(c in seq for c in "0123456789"):
        keypad = keypad_numeric
    else:
        keypad = keypad_directional

    count = 0
    for shortestPaths in buildSequence(seq, keypad):
        count += min(
            solveSequence(shortestPath, depth - 1) for shortestPath in shortestPaths
        )
    return count


def part_a(data):
    data = data.split("\n")

    count = 0
    for line in data:
        count += int(line[:3]) * solveSequence(line, 1 + 2)

    return count


def part_b(data):
    data = data.split("\n")

    count = 0
    for line in data:
        count += int(line[:3]) * solveSequence(line, 1 + 25)

    return count


if __name__ == "__main__":
    puzzle = Puzzle(2024, 21)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
