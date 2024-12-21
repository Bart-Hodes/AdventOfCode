from aocd.models import Puzzle

import re


def inputParser(lines):

    variables = {}
    instructions = []
    for line in lines:
        if line[0].isdigit():  # 456 -> y
            print(line)
            match = re.match(r"(\d+) -> (\w+)", line)
            variables[match.group(2)] = int(match.group(1))
            continue
        if line.startswith("NOT"):
            match = re.match(r"NOT (\w+) -> (\w+)", line)
            instructions.append(("NOT", match.group(1), match.group(2)))
            continue
        if "AND" in line:
            match = re.match(r"(\w+) AND (\w+) -> (\w+)", line)
            instructions.append(("AND", match.group(1), match.group(2), match.group(3)))
            continue
        if "OR" in line:
            match = re.match(r"(\w+) OR (\w+) -> (\w+)", line)
            instructions.append(("OR", match.group(1), match.group(2), match.group(3)))
            continue
        if "LSHIFT" in line:
            match = re.match(r"(\w+) LSHIFT (\d+) -> (\w+)", line)
            instructions.append(
                ("LSHIFT", match.group(1), match.group(2), match.group(3))
            )
            continue
        if "RSHIFT" in line:
            match = re.match(r"(\w+) RSHIFT (\d+) -> (\w+)", line)
            instructions.append(
                ("RSHIFT", match.group(1), match.group(2), match.group(3))
            )
            continue
    return variables, instructions


def NOT(variables, instruction):
    if instruction[1] in variables:
        variables[instruction[2]] = ~variables[instruction[1]]
    else:
        return None


def AND(variables, instruction):
    if instruction[1] in variables and instruction[2] in variables:
        variables[instruction[3]] = (
            variables[instruction[1]] & variables[instruction[2]]
        )
    else:
        return None


def OR(variables, instruction):
    if instruction[1] in variables and instruction[2] in variables:
        variables[instruction[3]] = (
            variables[instruction[1]] | variables[instruction[2]]
        )
    else:
        return None


def LSHIFT(variables, instruction):
    if instruction[1] in variables:
        variables[instruction[3]] = variables[instruction[1]] << int(instruction[2])
    else:
        return None


def RSHIFT(variables, instruction):
    if instruction[1] in variables:
        variables[instruction[3]] = variables[instruction[1]] >> int(instruction[2])
    else:
        return None


def evaluate(variables, instructions):

    for instruction in instructions:
        if instruction[0] == "NOT":
            NOT(variables, instruction)
        elif instruction[0] == "AND":
            AND(variables, instruction)
        elif instruction[0] == "OR":
            OR(variables, instruction)
        elif instruction[0] == "LSHIFT":
            LSHIFT(variables, instruction)
        elif instruction[0] == "RSHIFT":
            RSHIFT(variables, instruction)
        else:
            continue

    return variables


def part_a(data):
    lines = data.split("\n")

    variables, instructions = inputParser(lines)

    variables = evaluate(variables, instructions)

    for variable in variables:
        if variables[variable] < 0:
            variables[variable] = variables[variable] + 2**16

    return variables["a"]


def part_b(data):

    return None


if __name__ == "__main__":
    puzzle = Puzzle(2015, 7)
    examples = puzzle.examples
    # for example in examples:
    # print(example.answer_a)
    # print(part_a(example.input_data))

    puzzle.answer_a = part_a(puzzle.input_data)
