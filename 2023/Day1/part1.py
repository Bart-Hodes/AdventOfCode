import re

f = open("2023/Day1/input.txt", "r")

total = 0
for line in f:
    # Match first digit
    first_digit_match = re.search(r"\d", line)
    first_digit = first_digit_match.group(0) if first_digit_match else None

    # Match last digit
    last_digit_match = re.search(r"\d(?=[^\d]*$)", line)
    last_digit = last_digit_match.group(0) if last_digit_match else None

    total += int(first_digit + last_digit)

print(total)
