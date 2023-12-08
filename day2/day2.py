import re

def day2func():
    f = open("day2data.txt", "r")
    content = f.read().split("\n")

    # parse data into a list of dictionaries
    # {"Game": 1, "red": 7, "blue": 14, "green": 3}

    gameList = []

    maxRed, maxGreen, maxBlue = 12, 13, 14

    for a in content:
        print(a)

    res = 0

    # for game in content:
    #     rounds = game.split(";")
    #
    #     impossible = False
    #     for game_round in rounds:
    #         green = int(next(iter(re.findall("[0-9]+(?=\s+green)", game_round)), 0))
    #         blue = int(next(iter(re.findall("[0-9]+(?=\s+blue)", game_round)), 0))
    #         red = int(next(iter(re.findall("[0-9]+(?=\s+red)", game_round)), 0))
    #
    #         if red > maxRed or green > maxGreen or blue > maxBlue:
    #             impossible = True
    #             break
    #
    #     if impossible == False:
    #         gameId = int(re.findall("(?<=Game\s)[0-9]+", game)[0])
    #         res += gameId

    for game in content:
        rounds = game.split(";")

        impossible = False

        minGreen = 0
        minBlue = 0
        minRed = 0

        for game_round in rounds:
            green = int(next(iter(re.findall("[0-9]+(?=\s+green)", game_round)), 0))
            blue = int(next(iter(re.findall("[0-9]+(?=\s+blue)", game_round)), 0))
            red = int(next(iter(re.findall("[0-9]+(?=\s+red)", game_round)), 0))

            minGreen = max(green, minGreen)
            minBlue = max(blue, minBlue)
            minRed = max(red, minRed)

        res += (minGreen * minBlue * minRed)
    print("Hello")
    return res