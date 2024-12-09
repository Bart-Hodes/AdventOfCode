# I dont like the way this works, but it works

def is_valid_update(update, rules):
    valid = False
    swap = False
    while not valid:
        valid = True
        for x, y in rules:
            # If both pages x and y are in the update, ensure x comes before y
            if x in update and y in update:
                if update.index(x) > update.index(y):
                    valid = False
                    swap = True
                    # Swap numbers
                    update[update.index(x)], update[update.index(y)] = (
                        update[update.index(y)],
                        update[update.index(x)],
                    )
    return swap


with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# Parse input
rules = set()
updates = []
parsing_rules = True

for line in lines:
    if line == "":
        parsing_rules = False
        continue
    if parsing_rules:
        x, y = map(int, line.split("|"))
        rules.add((x, y))
    else:
        updates.append(list(map(int, line.split(","))))

# Validate updates and calculate the result
valid_middle_pages = []

for update in updates:
    if is_valid_update(update, rules):
        # Even number of pages is rounded down
        valid_middle_pages.append(update[len(update) // 2])

    if is_valid_update(update, rules):
        print(update, "is valid")
    else:
        print(update, "is invalid")

# Calculate the total of the middle pages
print(sum(valid_middle_pages))
