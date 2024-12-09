import re
import math

with open("input.txt", "r") as puzzleInput:
    lines = puzzleInput.read().split("\n")
    
pattern = r"Card\s+\d+:\s([\d\s]+)\|\s([\d\s]+)"

count = 0
for line in lines:
    match = re.search(pattern, line)
    
    left_numbers = set(match.group(1).split())
    right_numbers = set(match.group(2).split())

    subcount = 0
    for num in left_numbers:
        if num in right_numbers:
            subcount += 1
    if subcount > 0:
        count += 2**(subcount-1)
    
print(count)