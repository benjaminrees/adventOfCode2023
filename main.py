import re
from collections import defaultdict
from functools import cmp_to_key

from day2.day2 import day2func

f = open("day7data.txt", "r")
content = f.read().split("\n")

cardStrength = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}
for i in range(1, 10):
    cardStrength[str(i)] = i

# print(cardStrength)

# remove 0 to get list back
hands = [i.split() for i in content]
print(hands)

def countCards(hand):
    currentHand = hand
    cardCount = []
    for card in hand:
        cardCount.append(currentHand.count(card))
        currentHand = currentHand.replace(card, "")
    return sorted(cardCount, reverse=True)


def compareHands(firstHand, secondHand):
    firstHand = firstHand[0]
    secondHand = secondHand[0]

    firstCount = countCards(firstHand)
    secondCount = countCards(secondHand)

    # print("Counts")
    # print(firstCount)
    # print(secondCount)

    for i in range(0, 5):
        if firstCount[i] > secondCount[i]:
            return -1
        if firstCount[i] < secondCount[i]:
            return 1

    # if not returned yet, compare each card individually
    for i in range(0, 5):
        # print("comaparing " + str(cardStrength[firstHand[i]]) + " and " + str(cardStrength[secondHand[i]]))
        if cardStrength[firstHand[i]] > cardStrength[secondHand[i]]:
            return -1
        if cardStrength[firstHand[i]] < cardStrength[secondHand[i]]:
            return 1

hands = sorted(hands, key=cmp_to_key(compareHands), reverse=True)

res = 0
count = 1
for hand in hands:
    res += int(hand[1]) * count
    count += 1

print(res)