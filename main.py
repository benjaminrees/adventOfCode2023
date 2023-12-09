import re
from collections import defaultdict

from day2.day2 import day2func

f = open("day7data.txt", "r")
content = f.read().split("\n")

cardStrength = {"A": 14, "K": 13, "Q": 12, "J": 11, "T": 10}

for i in range(0, 10):
    cardStrength[str(i)] = i

hands = [i.split() for i in content]

# order each hand based on strength (you could probably condense to one line)
for game in range(0, len(hands)):
    hands[game][0] = "".join(sorted(hands[game][0], key=lambda x: cardStrength[x], reverse=True))

# precedence
# single pair
# two pair
# 3 of a kind
# could be done with bubble sort

# assign a score for each hand and rank by that
# compare 2 cards, compare for 4, 3, 2 pairs, then highest card