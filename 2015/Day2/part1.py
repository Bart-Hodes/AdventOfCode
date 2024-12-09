with open("2015/Day2/input.txt") as f:
    data = [line.strip("\n") for line in f.readlines()]


feetOfWrappingPaper = 0
for input in data:
    dimensions = input.split("x")

    side1 = 2 * int(dimensions[0]) * int(dimensions[1])
    side2 = 2 * int(dimensions[1]) * int(dimensions[2])
    side3 = 2 * int(dimensions[2]) * int(dimensions[0])

    feetOfWrappingPaper += side1 + side2 + side3 + min(side1, side2, side3) // 2

print(feetOfWrappingPaper)
