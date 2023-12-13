import math
import re
import time
from functools import cmp_to_key
from day2.day2 import day2func
from getNextPipe import getNextPipe, printGrid

f = open("day10/day10data.txt", "r")
grid = f.read().split("\n")

for line in range(0, len(grid)):
    if "S" in grid[line]:
        S = (line, grid[line].find("S"))

distances = [["."] * len(i) for i in grid]

def isNumber(stringNumber):
    if 48 >= ord(stringNumber) <= 57:
        return True
    return False

print("S location")
print(S)
distances[S[0]][S[1]] = "S"


# first pass
count = 0
nextLocation = (S[0] + 1, S[1])
direction = "S"

while grid[nextLocation[0]][nextLocation[1]] != ".":
    count += 1
    distances[nextLocation[0]][nextLocation[1]] = count
    direction, nextLocation = getNextPipe(grid, direction, nextLocation)

    if distances[nextLocation[0]][nextLocation[1]] == "S":
        print("broken")
        break

printGrid(distances)

print("part 2")
# count = 0
# nextLocation = (S[0], S[1] + 1)
#
# while grid[nextLocation[0]][nextLocation[1]] != ".":
#     count += 1
#     if distances[nextLocation[0]][nextLocation[1]] == count:
#         print("half reached")
#         break
#
#     distances[nextLocation[0]][nextLocation[1]] = count
#     direction, nextLocation = getNextPipe(grid, direction, nextLocation)
#
#     if grid[nextLocation[0]][nextLocation[1]] == "S":
#         break
#
# printGrid(distances)
# print(count)
#
# enclosedTiles = 0

# number of tiles enclosed by the loop
# find a number, count tiles, then stop count when you find another number
# how do we know that it isn't connected to the outside loop?
# find a way to mark all the tiles that are connected to the outside - some recursive algorith?
# then count the dots that haven't been converted

print("Conversion")
def convertDots(grid, dotLocation):
    dotGrid = [(0,0)]

    i = dotLocation[0]
    j = dotLocation[1]
    # printGrid(distances)

    print("Current dot")
    print(str(i) + " " + str(j))

    # up
    if i - 1 >= 0:
        nextDot = grid[i - 1][j]
        if nextDot == ".":
            grid[i - 1][j] = "*"
            # convertDots(grid, (i - 1, j))
            dotGrid.append((i - 1, j))


    # down
    if i + 1 < len(grid):
        nextDot = grid[i + 1][j]
        if nextDot == ".":
            grid[i + 1][j] = "*"
            # convertDots(grid, (i + 1, j))
            dotGrid.append((i + 1, j))
    # left
    if j - 1 >= 0:
        nextDot = grid[i][j - 1]
        if nextDot == ".":
            grid[i][j - 1] = "*"
            # convertDots(grid, (i, j - 1))
            dotGrid.append((i, j - 1))


    # right
    if j + 1 < len(grid[0]):
        nextDot = grid[i][j + 1]
        if nextDot == ".":
            grid[i][j + 1] = "*"
            convertDots(grid, (i, j + 1))

    return


convertDots(distances, (0,0))
printGrid(distances)
