from aocd.models import Puzzle


def mix(givenValue, secretValue):
    return givenValue ^ secretValue


def prune(secretValue):
    return secretValue % 16777216


def process1(secretValue):
    secretValue = mix(secretValue, secretValue * 64)
    secretValue = prune(secretValue)
    return secretValue


def process2(secretValue):
    givenValue = secretValue // 32
    secretValue = mix(secretValue, givenValue)
    secretValue = prune(secretValue)
    return secretValue


def process3(secretValue):
    secretValue = mix(secretValue, secretValue * 2048)
    secretValue = prune(secretValue)
    return secretValue


def psuedoRandomGenerator(secretValue):
    secretValue = process1(secretValue)
    secretValue = process2(secretValue)
    secretValue = process3(secretValue)
    return secretValue


def psuedoRandomSequence(secretValue, lenght):
    sequence = []
    for _ in range(lenght):
        secretValue = psuedoRandomGenerator(secretValue)
        sequence.append(secretValue)
    return sequence


def part_a(data):
    lines = data.split("\n")

    count = 0
    for startingValue in lines:
        startingValue = int(startingValue)
        sequence = psuedoRandomSequence(startingValue, 2000)
        count += sequence[1999]

    return count


def diffSequence(sequence):
    diff = []
    for i in range(len(sequence) - 1):
        diff.append(sequence[i + 1] % 10 - sequence[i] % 10)
    return diff


def sequenceBananas(sequence):
    bananaDiffDict = {}
    diff = diffSequence(sequence)

    for idx, sequenceItem in enumerate(sequence):
        numBananas = sequenceItem % 10
        diff_tuple = tuple(diff[idx - 4 : idx])
        if len(diff_tuple) < 4:
            continue
        if diff_tuple == ():
            print(idx)
            quit()
        if diff_tuple not in bananaDiffDict:
            bananaDiffDict[diff_tuple] = int(numBananas)
    return bananaDiffDict


def combine_dicts(dict1, dict2):
    combined_dict = {}
    all_keys = set(dict1.keys()).union(dict2.keys())

    for key in all_keys:
        if key in dict1 and key in dict2:
            combined_dict[key] = int(dict1[key] + dict2[key])
        elif key in dict1:
            combined_dict[key] = dict1[key]
        else:  # key in dict2
            combined_dict[key] = dict2[key]

    return combined_dict


def part_b(data):
    lines = data.split("\n")

    dictionary = {(0, 0, 0, 0): 0}

    for startingValue in lines:
        startingValue = int(startingValue)
        sequence = psuedoRandomSequence(startingValue, 2000)
        sequence.insert(0, startingValue)
        diffDict = sequenceBananas(sequence)
        dictionary = combine_dicts(dictionary, diffDict)

    maxBananas = max(dictionary, key=dictionary.get)

    return dictionary[maxBananas]


if __name__ == "__main__":
    puzzle = Puzzle(2024, 22)
    puzzle.answer_a = part_a(puzzle.input_data)
    puzzle.answer_b = part_b(puzzle.input_data)
