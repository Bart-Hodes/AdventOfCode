from aocd.models import Puzzle


def printGrid(walls, boxes, robotPos):
    for y in range(7):
        for x in range(14):
            if (x, y) in walls:
                print("#", end="")
            elif (x, y) in boxes:
                print("O", end="")
            elif (x, y) == robotPos:
                print("@", end="")
            else:
                print(".", end="")
        print()


def printGrid2(walls, boxes, robotPos):
    for y in range(10):
        for x in range(20):
            if (x, y) in walls:
                print("#", end="")
            elif any((x, y) == pair[0] for pair in boxes):
                print("[", end="")
            elif any((x, y) == pair[1] for pair in boxes):
                print("]", end="")
            elif (x, y) == robotPos:
                print("@", end="")
            else:
                print(".", end="")
        print()


def part_a(data):

    grid, movements = data.split("\n\n")

    movements = movements.replace("\n", "")
    grid = grid.split("\n")

    walls = set()
    boxes = set()
    robotPos = None

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "#":
                walls.add((x, y))
            elif cell == "O":
                boxes.add((x, y))
            elif cell == "@":
                robotPos = (x, y)

    # Define movement offsets
    offsets = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0),
    }

    for move in movements:

        dx, dy = offsets[move]  # Get movement offset

        # Calculate next position
        next_pos = (robotPos[0] + dx, robotPos[1] + dy)

        # Check if movement hits a wall
        if next_pos in walls:
            continue

        # Check if there's a line of boxes and space to push them
        current_pos = next_pos
        box_positions = []  # Keep track of all consecutive boxes in the direction
        while current_pos in boxes:
            box_positions.append(current_pos)
            current_pos = (current_pos[0] + dx, current_pos[1] + dy)

        # If the end position is a wall or another box, pushing isn't possible
        if current_pos in walls or current_pos in boxes:
            continue

        # Move all boxes
        for box_pos in reversed(box_positions):  # Move boxes from back to front
            new_box_pos = (box_pos[0] + dx, box_pos[1] + dy)
            boxes.remove(box_pos)
            boxes.add(new_box_pos)

        # Update robot position
        robotPos = next_pos

    # Calculate laternfish gps score
    gpsScore = 0
    for box in boxes:

        gpsScore += box[0] + 100 * box[1]

    return gpsScore


def scale_map(original_map):
    scaled_map = []
    for row in original_map:
        scaled_row = ""
        for tile in row:
            if tile == "#":
                scaled_row += "##"
            elif tile == "O":
                scaled_row += "[]"
            elif tile == ".":
                scaled_row += ".."
            elif tile == "@":
                scaled_row += "@."
        scaled_map.append(scaled_row)
    return scaled_map


import time


def part_b(data):

    grid, movements = data.split("\n\n")
    movements = movements.replace("\n", "")
    grid = grid.split("\n")

    grid = scale_map(grid)

    walls = set()
    boxes = set()
    robotPos = None

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "#":
                walls.add((x, y))
            elif cell == "[":
                boxes.add(((x, y), (x + 1, y)))
            elif cell == "@":
                robotPos = (x, y)

    # Define movement offsets
    offsets = {
        "^": (0, -1),
        "v": (0, 1),
        "<": (-1, 0),
        ">": (1, 0),
    }

    for move in movements:
        # printGrid2(walls, boxes, robotPos)
        # print(move)

        dx, dy = offsets[move]  # Get movement offset

        # Calculate next position
        next_pos = (robotPos[0] + dx, robotPos[1] + dy)

        # Check if movement hits a wall
        if next_pos in walls:
            continue

        # Check if there's a line of boxes and space to push them
        current_pos = next_pos
        box_positions = (
            set()
        )  # Keep track of all consecutive boxes (pairs) in the direction
        positionsToCheck = []
        checkedPositions = set()

        positionsToCheck.extend([next_pos])

        while any(pos in pair for pos in positionsToCheck for pair in boxes):

            # Take value from positionsToCheck
            current_pos = positionsToCheck.pop(0)
            # Find the box pair occupying the position we try to move to
            for pair in boxes:
                if current_pos in pair and current_pos not in checkedPositions:
                    # This box needs to move
                    box_positions.add(pair)
                    positionsToCheck.extend(
                        [
                            (pair[0][0] + dx, pair[0][1] + dy),
                            (pair[1][0] + dx, pair[1][1] + dy),
                        ]
                    )
                    checkedPositions.add(current_pos)
                    break  # Only one box can contain a given position at a time

        # # If the end position is a wall or overlaps any other box, pushing isn't possible
        # if current_pos in walls or any(current_pos in pair for pair in boxes):
        #     continue

        # Check if all new box positions are valid we need to translate the box positions by dx, dy
        box_movements_valid = True
        for box in box_positions:
            if (box[0][0] + dx, box[0][1] + dy) in walls or (
                box[1][0] + dx,
                box[1][1] + dy,
            ) in walls:
                box_movements_valid = False
                break
        if not box_movements_valid:
            continue

        # Move all boxes
        boxes_to_remove = []
        boxes_to_add = []
        for box_pair in box_positions:  # Move boxes from back to front
            new_pair = (
                (box_pair[0][0] + dx, box_pair[0][1] + dy),
                (box_pair[1][0] + dx, box_pair[1][1] + dy),
            )
            boxes_to_remove.append(box_pair)
            boxes_to_add.append(new_pair)

        for box in boxes_to_remove:
            boxes.remove(box)
        for box in boxes_to_add:
            boxes.add(box)
        # Update robot position
        robotPos = (robotPos[0] + dx, robotPos[1] + dy)

    # printGrid2(walls, boxes, robotPos)

    # Calculate laternfish gps score
    gpsScore = 0
    for box in boxes:
        gpsScore += box[0][0] + 100 * box[0][1]

    return gpsScore


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=15)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
