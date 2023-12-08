import re
from collections import defaultdict

from day2.day2 import day2func

f = open("day4data.txt", "r")
content = f.read().split("\n")

cards = []
for line in content:
    cards.append(line.split("|"))

totalPoints = 0

# for game in cards:
#     # take everything to the right of :
#     game[0] = game[0].split(":")[1]
#     game[0] = list(re.findall("[0-9]+", game[0]))
#     game[1] = list(re.findall("[0-9]+", game[1]))
#
#     targets = set(game[0])
#     # winning numbers
#     points = 0
#     for number in game[1]:
#         if number in targets:
#             if points == 0:
#                 points = 1
#             else:
#                 points *= 2
#
#     totalPoints += points

cardCopies = dict()

for i in range(0, len(cards)):
    cardCopies[i+1] = 1

gameNumber = 1
for game in cards:

    game[0] = game[0].split(":")[1]
    game[0] = list(re.findall("[0-9]+", game[0]))
    game[1] = list(re.findall("[0-9]+", game[1]))

    targets = set(game[0])

    # find number of matches between numbers and target

    for k in range(0, cardCopies[gameNumber]):
        matches = 0
        for number in game[1]:
            if number in targets:
                matches += 1

        # add card for every match in subsequent cards
        for j in range(gameNumber + 1, gameNumber + matches + 1):
            cardCopies[j] += 1

    gameNumber += 1


for card in cardCopies:
    totalPoints += cardCopies[card.numerator]

print(cardCopies)
print(totalPoints)







