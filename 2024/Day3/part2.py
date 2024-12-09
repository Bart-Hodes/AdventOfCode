import re

f = open("2024/Day3/input.txt", "r")

counter = 0
enable = True

for line in f:
    matches = re.finditer("mul\((\d{1,3},\d{1,3})\)|do\(\)|don't\(\)", line)
    for match_obj in matches:
        print(match_obj.group())
        if match_obj.group() == "do()":
            enable = True
            continue
        if match_obj.group() == "don't()":
            enable = False
            continue
        if enable:
            values = match_obj.group(1).split(",")
            counter += int(values[0]) * int(values[1])

print(counter)
