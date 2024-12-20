from aocd.models import Puzzle


def comboOperant(operant, RegisterFile):
    # ComboOperant logic
    if operant < 4:
        operant = operant
    elif operant == 4:
        operant = RegisterFile[0]
    elif operant == 5:
        operant = RegisterFile[1]
    elif operant == 6:
        operant = RegisterFile[2]
    else:
        raise Exception("Invalid Operant")
    return operant


def adv(operant, RegisterFile):
    operant = comboOperant(operant, RegisterFile)
    RegisterFile[0] = int(RegisterFile[0] / 2**operant)
    return True


def bxl(operant, RegisterFile):
    RegisterFile[1] = RegisterFile[1] ^ operant
    return True


def bst(operant, RegisterFile):
    operant = comboOperant(operant, RegisterFile)
    RegisterFile[1] = operant % 8


def jnz(operant, RegisterFile):
    if RegisterFile[0] != 0:
        RegisterFile[3] = operant - 2
    return True


def bxc(operant, RegisterFile):
    RegisterFile[1] = RegisterFile[1] ^ RegisterFile[2]
    return True


def out(operant, RegisterFile):
    operant = comboOperant(operant, RegisterFile)
    outputBuffer.append(str(operant % 8))


def bdv(operant, RegisterFile):
    operant = comboOperant(operant, RegisterFile)
    RegisterFile[1] = int(RegisterFile[0] / 2**operant)
    return True


def cdv(operant, RegisterFile):
    operant = comboOperant(operant, RegisterFile)
    RegisterFile[2] = int(RegisterFile[0] / 2**operant)
    return True


def part_a(data):
    global outputBuffer
    outputBuffer = []

    lines = data.split("\n")
    RegisterA = int(lines[0].split(": ")[1])
    RegisterB = int(lines[1].split(": ")[1])
    RegisterC = int(lines[2].split(": ")[1])
    programPointer = 0
    RegisterFile = [RegisterA, RegisterB, RegisterC, programPointer]

    Program = lines[4].strip("Program: ")
    Program = Program.split(",")

    debugcounter = 0
    while RegisterFile[3] < len(Program):
        command = Program[RegisterFile[3]]
        operant = Program[RegisterFile[3] + 1]
        # print(command, operant, RegisterFile)
        if command == "0":
            adv(int(operant), RegisterFile)
        elif command == "1":
            bxl(int(operant), RegisterFile)
        elif command == "2":
            bst(int(operant), RegisterFile)
        elif command == "3":
            jnz(int(operant), RegisterFile)
        elif command == "4":
            bxc(int(operant), RegisterFile)
        elif command == "5":
            out(int(operant), RegisterFile)
        elif command == "6":
            bdv(int(operant), RegisterFile)
        elif command == "7":
            cdv(int(operant), RegisterFile)
        RegisterFile[3] += 2
    return ",".join(outputBuffer)


def part_b(data):

    data = data.split("\n")
    programOutput = data[4][9:].split(",")
    programOutput.reverse()

    def find_final_regA(data, programOutput, regA, idx):
        # Base case: all digits in programOutput have been processed
        if idx == len(programOutput):
            return regA / 8  # We multiply once to many in the recursion

        digit = programOutput[idx]

        # Try all possible values for checkDigit
        for checkDigit in range(0, 8):
            data[0] = f"Register A: {checkDigit + regA}"
            output = part_a("\n".join(data))

            # If output[0] matches the current digit, proceed with recursion
            if output[0] == digit:
                newRegA = (regA + int(checkDigit)) * 8
                result = find_final_regA(data, programOutput, newRegA, idx + 1)
                if result is not None:
                    return (
                        result  # Return the final regA once a valid sequence is found
                    )

        return None  # No valid continuation found

    # Start the recursive search from the first digit
    return int(find_final_regA(data, programOutput, regA=0, idx=0))


if __name__ == "__main__":
    puzzle = Puzzle(year=2024, day=17)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
