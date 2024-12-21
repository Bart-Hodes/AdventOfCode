from aocd.models import Puzzle

import re


def part_a(data):
    lines = data.split("\n")

    maxRed = 12
    maxGreen = 13
    maxBlue = 14

    count = 0

    for line in lines:
        # Remove line header
        gameInfo = line.split(":")
        subset = gameInfo[1].split(";")

        # Initial assumption game valid
        valid = True

        minRed = 0
        minGreen = 0
        minBlue = 0
        for game in subset:
            match = re.search("((\d*) red)", game)
            if match != None:
                numRed = int(match.group(2))
            else:
                numRed = 0
            match = re.search("((\d*) blue)", game)
            if match != None:
                numBlue = int(match.group(2))
            else:
                numBlue = 0
            match = re.search("((\d*) green)", game)
            if match != None:
                numGreen = int(match.group(2))
            else:
                numGreen = 0

            # Check game validity
            if not (numRed <= maxRed and numBlue <= maxBlue and numGreen <= maxGreen):
                valid = False

        if valid:
            gameIdx = re.search("(Game (\d*))", gameInfo[0]).group(2)
            count += int(gameIdx)

    return count


def part_b(data):
    lines = data.split("\n")

    count = 0

    for line in lines:
        # Remove line header
        gameInfo = line.split(":")
        subset = gameInfo[1].split(";")

        minRed = 0
        minGreen = 0
        minBlue = 0
        for game in subset:
            match = re.search("((\d*) red)", game)
            if match != None:
                numRed = int(match.group(2))
            else:
                numRed = 0
            match = re.search("((\d*) blue)", game)
            if match != None:
                numBlue = int(match.group(2))
            else:
                numBlue = 0
            match = re.search("((\d*) green)", game)
            if match != None:
                numGreen = int(match.group(2))
            else:
                numGreen = 0

            if minRed < numRed:
                minRed = numRed
            if minBlue < numBlue:
                minBlue = numBlue
            if minGreen < numGreen:
                minGreen = numGreen

        count += minRed * minBlue * minGreen

    return count


if __name__ == "__main__":
    puzzle = Puzzle(2023, 2)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
