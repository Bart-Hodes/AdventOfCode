import re

f = open("2024/Day3/input.txt", "r")

counter = 0
for line in f:
    matches = re.finditer("mul\((\d{1,3},\d{1,3})\)", line)
    for match_obj in matches:
        values = match_obj.group(1).split(",")
        counter += int(values[0]) * int(values[1])

print(counter)
