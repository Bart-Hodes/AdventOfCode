from aocd import data
from aocd.models import Puzzle
import re


def x_to_x_Map(seedId, rule):
    if int(rule[1]) <= int(seedId) < int(rule[1]) + int(rule[2]):
        seedId = int(rule[0]) + (int(seedId) - int(rule[1]))
        return seedId, True
    return seedId, False


def map_range(start, length, rule):
    """
    Map a range (start, length) using a single rule.
    Returns a list of new ranges after mapping, splitting only when needed.
    """
    dest_start, src_start, rule_length = map(int, rule)
    src_end = src_start + rule_length - 1
    mapped_ranges = []

    # If the range does not intersect the rule, it remains unchanged
    range_end = start + length - 1
    if range_end < src_start or start > src_end:
        return [(start, length)]

    # Handle intersection: Split range if needed
    if start < src_start:
        mapped_ranges.append((start, src_start - start))  # Before the mapped range

    if start <= src_end <= range_end:
        # Partial or full overlap: Map the intersecting range
        overlap_start = max(start, src_start)
        overlap_length = min(src_end, range_end) - overlap_start + 1
        mapped_start = dest_start + (overlap_start - src_start)
        mapped_ranges.append((mapped_start, overlap_length))

    if range_end > src_end:
        # After the mapped range
        mapped_ranges.append((src_end + 1, range_end - src_end))

    return mapped_ranges


def part_a(data):
    lines = data.split("\n")
    lines[-1] += "\n"

    seedIds = re.findall(r"\d+", lines[0])
    seedIds = [int(seedId) for seedId in seedIds]

    # Get maps
    Maps = re.findall(r"(?:\d+ \d+ \d+\n)+", "\n".join(lines[1:]), re.MULTILINE)
    for map in Maps:
        for idx, seedId in enumerate(seedIds):
            for rule in map.split("\n"):
                if rule:
                    seedIds[idx], Mutable = x_to_x_Map(seedId, rule.split(" "))
                    if Mutable:
                        break
    return min(seedIds)


def part_b(data):
    lines = data.split("\n")
    lines[-1] += "\n"

    # Parse seed ranges from the first line
    seedRanges = re.findall(r"\d+", lines[0])
    seed_ranges = []
    for i in range(0, len(seedRanges), 2):
        start = int(seedRanges[i])
        length = int(seedRanges[i + 1])
        seed_ranges.append((start, length))

    # Get maps
    Maps = re.findall(r"(?:\d+ \d+ \d+\n)+", "\n".join(lines[1:]), re.MULTILINE)

    for map_data in Maps:
        new_ranges = []
        for start, length in seed_ranges:
            for rule in map_data.splitlines():
                if rule.strip():
                    new_ranges.extend(map_range(start, length, rule.split()))
        seed_ranges = new_ranges

    seedIds = [start for start, length in seed_ranges]
    return min(seedIds)


if __name__ == "__main__":
    puzzle = Puzzle(2023, 5)
    # puzzle.answer_a = part_a(data)
    puzzle.answer_b = part_b(data)
