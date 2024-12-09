with open("2015/Day1/input.txt", "r") as f:
    sequence = f.readline()

count = 0
for char in sequence:
    if char == "(":
        count += 1
    elif char == ")":
        count -= 1


print(count)
