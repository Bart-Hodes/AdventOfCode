import itertools

operators = ["*", "+","||"]
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# print(lines)

count = 0
for line in lines:
    contents = line.split(":")
    result = contents[0]
    values = contents[1].split(" ")[1:]

    permutations = list(itertools.product([0,1,2], repeat = len(values)-1))
    for perm in permutations:
        workingSet = values.copy()
        product = workingSet[0]
        for idx in range(len(perm)):
            if perm[idx] == 0:
                product = int(product) * int(workingSet[idx+1])
            elif perm[idx] == 1:
                product = int(product) + int(workingSet[idx+1])
            elif perm[idx] == 2:
                product = str(product) + workingSet[idx+1]
                
        if int(product) == int(result):
            count += int(result)
            break

print(f"count is {count}")
    # Brute force search


