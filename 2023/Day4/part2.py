import re
import math

with open("input.txt", "r") as puzzleInput:
    lines = puzzleInput.read().split("\n")
    
pattern = r"Card\s+\d+:\s([\d\s]+)\|\s([\d\s]+)"

cards = []
for line in lines:
    match = re.search(pattern, line)
    
    left_numbers = set(match.group(1).split())
    right_numbers = set(match.group(2).split())
    
    cards.append([left_numbers, right_numbers])
    
    
card_copies = [1]*len(cards)

for idx, card in enumerate(cards):
    subcount = 1
    for num in card[0]:
        if num in card[1]:
            card_copies[idx+subcount] += card_copies[idx]
            subcount += 1
print(sum(card_copies))
