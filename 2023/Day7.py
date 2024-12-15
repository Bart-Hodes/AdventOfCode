from aocd.models import Puzzle

from collections import Counter


def sortHands(hands):
    hands.sort()
    hands.sort(key=lambda x: (sorted(list(Counter(x[0]).values()), reverse=True), x))


def sortHandsWithJoker(hands):
    hands.sort()

    for idx, hand in enumerate(hands):
        for card in hand[0]:
            if card == "1":
                count = Counter(hand[0])
                hand_list = list(hands[idx])
                if count.most_common()[0][1] == "1":
                    hand_list[0] = hand_list[0].replace(
                        "1", str(count.most_common()[1][0])
                    )
                else:
                    hand_list[0] = hand_list[0].replace(
                        "1", str(count.most_common()[0][0])
                    )
                print(hand_list)
                hands[idx] = tuple(hand_list)

    hands.sort(key=lambda x: (sorted(list(Counter(x[0]).values()), reverse=True), x))


def part_a(data):
    lines = data.split("\n")

    hands = []
    for line in lines:
        cards, bid = line.split(" ")
        # Replace A K Q J T with 14 13 12 11 10
        cards = cards.replace("A", "F")
        cards = cards.replace("K", "E")
        cards = cards.replace("Q", "D")
        cards = cards.replace("J", "C")
        cards = cards.replace("T", "B")

        hands.append((cards, bid))

    sortHands(hands)

    totalWinnings = 0
    for idx, (card, bid) in enumerate(hands):
        totalWinnings += int(bid) * (idx + 1)

    return totalWinnings


def part_b(data):
    data = """2345A 1
Q2KJJ 13
Q2Q2Q 19
T3T3J 17
T3Q33 11
2345J 3
J345A 2
32T3K 5
T55J5 29
KK677 7
KTJJT 34
QQQJA 31
JJJJJ 37
JAAAA 43
AAAAJ 59
AAAAA 61
2AAAA 23
2JJJJ 53
JJJJ2 41"""

    lines = data.split("\n")

    hands = []
    for line in lines:
        cards, bid = line.split(" ")
        # Replace A K Q J T with 14 13 12 11 10
        cards = cards.replace("A", "F")
        cards = cards.replace("K", "E")
        cards = cards.replace("Q", "D")
        cards = cards.replace("J", "1")
        cards = cards.replace("T", "B")

        hands.append((cards, bid))

    sortHandsWithJoker(hands)

    print(hands)

    totalWinnings = 0
    for idx, (card, bid) in enumerate(hands):
        totalWinnings += int(bid) * (idx + 1)

    print(totalWinnings)

    return totalWinnings


if __name__ == "__main__":
    puzzle = Puzzle(2023, 7)
    examples = puzzle.examples
    for example in examples:
        part_b(example.input_data)
    # puzzle.answer_a = part_a(puzzle.input_data)
    # puzzle.answer_b = part_b(puzzle.input_data)
