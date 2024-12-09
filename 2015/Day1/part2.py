with open("input.txt", "r") as f:
    sequence = f.readline()

count = 0
for idx, char in enumerate(sequence):
    if char == "(":
        count += 1
    elif char == ")":
        count -= 1
    if count < 0:
        print(idx + 1)
        break
