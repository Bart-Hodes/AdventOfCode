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


with open("2024/Day2/input.txt", "r") as f:
    reports = []
    for line in f:
        report = list(map(int, line.strip().split()))
        reports.append(report)

# Count safe reports
safe_count = 0

for report in reports:
    if is_safe(report) or can_be_made_safe_by_removing_one_level(report):
        safe_count += 1

print(f"Number of safe reports with the Problem Dampener: {safe_count}")
