from aocd.models import Puzzle


def is_safe(levels):
    # Check if all increasing or all decreasing
    increasing = all(x < y for x, y in zip(levels, levels[1:]))
    decreasing = all(x > y for x, y in zip(levels, levels[1:]))

    # Check the difference between adjacent levels
    diffs = [abs(x - y) for x, y in zip(levels, levels[1:])]

    if increasing or decreasing:
        return all(1 <= diff <= 3 for diff in diffs)
    else:
        return False


def can_be_made_safe_by_removing_one_level(levels):
    n = len(levels)
    for i in range(n):
        # Remove the i-th level
        new_levels = levels[:i] + levels[i + 1 :]
        if is_safe(new_levels):
            return True
    return False


def part_a(data):
    data = data.split("\n")

    reports = []
    for line in data:
        report = list(map(int, line.strip().split()))
        reports.append(report)

    # Count safe reports
    safe_count = 0

    for report in reports:
        if is_safe(report):
            safe_count += 1

    return safe_count


def part_b(data):
    data = data.split("\n")

    reports = []
    for line in data:
        report = list(map(int, line.strip().split()))
        reports.append(report)

    # Count safe reports
    safe_count = 0

    for report in reports:
        if is_safe(report) or can_be_made_safe_by_removing_one_level(report):
            safe_count += 1

    return safe_count


if __name__ == "__main__":
    puzzle = Puzzle(2024, 2)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
