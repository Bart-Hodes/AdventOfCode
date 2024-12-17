def run(regA):
    global Output
    RegA, RegB, RegC, IP, Output = regA, int(Lines[1][12:]), int(Lines[2][12:]), 0, []
    while IP < len(Prog):
        instr, operand = Prog[IP]
        match instr:
            case 0:
                RegA = RegA // (
                    2 ** [operand, operand, operand, operand, RegA, RegB, RegC][operand]
                )
            case 1:
                RegB = RegB ^ operand
            case 2:
                RegB = [operand, operand, operand, operand, RegA, RegB, RegC][
                    operand
                ] % 8
            case 3:
                IP = operand - 1 if RegA != 0 else IP
            case 4:
                RegB = RegB ^ RegC
            case 5:
                Output.append(
                    RegB := [operand, operand, operand, operand, RegA, RegB, RegC][
                        operand
                    ]
                    % 8
                )
            case 6:
                RegB = RegA // (
                    2 ** [operand, operand, operand, operand, RegA, RegB, RegC][operand]
                )
            case 7:
                RegC = RegA // (
                    2 ** [operand, operand, operand, operand, RegA, RegB, RegC][operand]
                )
        IP += 1
