def getNextPipe(grid, direction, pipeLocation):
    i = pipeLocation[0]
    j = pipeLocation[1]

    if direction == "N":
        if grid[i][j] == "|":
            return direction, [i - 1, j]
        if grid[i][j] == "7":
            direction = "W"
            return direction, [i, j - 1]
        if grid[i][j] == "F":
            direction = "E"
            return direction, [i, j + 1]

    if direction == "S":
        if grid[i][j] == "|":
            return direction, [i + 1, j]
        if grid[i][j] == "L":
            direction = "E"
            return direction, [i, j + 1]
        if grid[i][j] == "J":
            direction = "W"
            return direction, [i, j - 1]

    if direction == "E":
        if grid[i][j] == "-":
            return direction, [i, j + 1]
        if grid[i][j] == "J":
            direction = "N"
            return direction, [i - 1, j]
        if grid[i][j] == "7":
            direction = "S"
            return direction, [i + 1, j]

    if direction == "W":
        if grid[i][j] == "-":
            return direction, [i, j - 1]
        if grid[i][j] == "L":
            direction = "N"
            return direction, [i - 1, j]
        if grid[i][j] == "F":
            direction = "S"
            return direction, [i + 1, j]

    return direction, pipeLocation

def printGrid(grid):
    for i in grid:
        # print("".join(str(j) for j in i))
        print(i)
    print("")
