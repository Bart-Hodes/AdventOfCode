with open("2015/Day2/input.txt") as f:
    data = [line.strip("\n") for line in f.readlines()]


feetOfRibbon = 0
for input in data:
    dimensions = input.split("x")

    dimensions = [int(dimension) for dimension in dimensions]
    dimensions.sort()

    feetOfRibbon += (
        dimensions[0] * dimensions[1] * dimensions[2]
        + 2 * dimensions[0]
        + 2 * dimensions[1]
    )

print(feetOfRibbon)
