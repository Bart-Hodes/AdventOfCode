from aocd import data
from aocd.models import Puzzle


def is_valid_update(update, rules):
    for x, y in rules:
        # If both pages x and y are in the update, ensure x comes before y
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


def is_valid_update_part_b(update, rules):
    valid = False
    swap = False
    while not valid:
        valid = True
        for x, y in rules:
            # If both pages x and y are in the update, ensure x comes before y
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    valid = False
                    swap = True
                    # Swap numbers
                    update[update.index(x)], update[update.index(y)] = (
                        update[update.index(y)],
                        update[update.index(x)],
                    )
    return swap


def part_a(data):
    data = data.split("\n")

    # Parse input
    rules = set()
    updates = []
    parsing_rules = True

    for line in data:
        if line == "":
            parsing_rules = False
            continue
        if parsing_rules:
            x, y = map(int, line.split("|"))
            rules.add((x, y))
        else:
            updates.append(list(map(int, line.split(","))))

    # Validate updates and calculate the result
    valid_middle_pages = []

    for update in updates:
        if is_valid_update(update, rules):
            # Even number of pages is rounded down
            valid_middle_pages.append(update[len(update) // 2])

    # Calculate the total of the middle pages
    return sum(valid_middle_pages)


def part_b(data):
    data = data.split("\n")

    # Parse input
    rules = set()
    updates = []
    parsing_rules = True

    for line in data:
        if line == "":
            parsing_rules = False
            continue
        if parsing_rules:
            x, y = map(int, line.split("|"))
            rules.add((x, y))
        else:
            updates.append(list(map(int, line.split(","))))

    # Validate updates and calculate the result
    valid_middle_pages = []

    for update in updates:
        if is_valid_update_part_b(update, rules):
            # Even number of pages is rounded down
            valid_middle_pages.append(update[len(update) // 2])

    # Calculate the total of the middle pages
    return sum(valid_middle_pages)


if __name__ == "__main__":
    puzzle = Puzzle(2024, 5)
    # for example in puzzle.examples:
    #     if example.answer_a:
    #         if int(example.answer_a) != part_a(example.input_data):
    #             print("Example part A failed!")
    #             print(f"Expected: {example.answer_a}")
    #             print(f"Got: {part_a(example.input_data)}")
    # if example.answer_b:
    #     if int(example.answer_b) != part_b(example.input_data):
    #         print("Example part B failed!")
    #         print(example)
    #         print(f"Expected: {example.answer_b}")
    #         print(f"Got: {part_b(example.input_data)}")
    puzzle.answer_a = part_a(data)
    puzzle.answer_b = part_b(data)
