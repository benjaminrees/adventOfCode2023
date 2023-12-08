import re
from collections import defaultdict

f = open("day3data.txt", "r")
content = f.read().split("\n")


def isSymbol(char):
    if 48 <= ord(char) <= 57:
        return False
    elif 65 <= ord(char) <= 90:
        return False
    elif 97 <= ord(char) <= 122:
        return False
    elif ord(char) == 46:
        return False
    else:
        return True


def searchAroundSpan(line, left, right):
    if left == 0:
        left = 1
    if right == 140:
        right = 139

    # search above unless first line
    if line > 0:
        for j in range(left - 1, right + 1):
            if isSymbol(content[line - 1][j]):
                return True

    # search across current line
    for j in range(left - 1, right + 1):
        if isSymbol(content[line][j]):
            return True

    # search below unless last line
    if line < len(content) - 1:
        for j in range(left - 1, right + 1):
            if isSymbol(content[line + 1][j]):
                return True

    return False


def part1():
    res = 0
    for i in range(0, len(content)):
        # match object returns ever instance of a number in a line
        # span gives start and end index of number in string
        matches = re.finditer("[0-9]+", content[i])

        for x in matches:
            if searchAroundSpan(i, x.span()[0], x.span()[1]):
                res += int((x.group()))

    print(res)


part1()


def searchForGear(line, left, right):
    if left == 0:
        left = 1
    if right == 140:
        right = 139

    # search above unless first line
    if line > 0:
        for j in range(left - 1, right + 1):
            if content[line - 1][j] == "*":
                return line - 1, j

    # search across current line
    for j in range(left - 1, right + 1):
        if content[line][j] == "*":
            return line, j

    # search below unless last line
    if line < len(content) - 1:
        for j in range(left - 1, right + 1):
            if content[line + 1][j] == "*":
                return line + 1, j

    return -1, -1


gearDict = dict(str)
res = 0

for i in range(0, len(content)):

    # match object returns ever instance of a number in a line
    # span gives start and end index of number in string
    matches = re.finditer("[0-9]+", content[i])

    for x in matches:
        gearLocation = searchForGear(i, x.span()[0], x.span()[1])
        if gearLocation != (-1, -1):
            if gearLocation in gearDict:
                res += int(x.group()) * int(gearDict[gearLocation])
            else:
                gearDict[gearLocation] = x.group()

print(gearDict)
print(res)
