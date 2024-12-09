import itertools

operators = ["*", "+"]
with open("input.txt", "r") as f:
    lines = [line.strip() for line in f.readlines()]

# print(lines)

count = 0
for line in lines:
    contents = line.split(":")
    result = contents[0]
    values = contents[1].split(" ")[1:]

    permutations = list(itertools.product([0,1], repeat = len(values)-1))
    for perm in permutations:
        product = values[0]
        for idx in range(len(perm)):
            product = eval(f"{product} {operators[perm[idx]]} {values[idx+1]}")

        if int(product) == int(result):
            print("Found")
            print(f"{result} = {values}")
            print(f"Permutation: {perm}")


            count += int(result)
            break

print(f"count is {count}")
    # Brute force search


