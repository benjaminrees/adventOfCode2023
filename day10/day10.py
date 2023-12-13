from getNextPipe import getNextPipe, printGrid


def day10func():
    f = open("day10/day10test.txt", "r")
    grid = f.read().split("\n")

    for line in range(0, len(grid)):
        if "S" in grid[line]:
            S = (line, grid[line].find("S"))

    distances = [["."] * len(i) for i in grid]


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

    maxCount = count
    print("MaxCount " + str(count))
    printGrid(distances)

    print("part 2")
    count = 0
    nextLocation = (S[0], S[1] + 1)

    while grid[nextLocation[0]][nextLocation[1]] != ".":
        count += 1
        if distances[nextLocation[0]][nextLocation[1]] == count:
            print("half reached")
            break

        distances[nextLocation[0]][nextLocation[1]] = count
        direction, nextLocation = getNextPipe(grid, direction, nextLocation)

        if grid[nextLocation[0]][nextLocation[1]] == "S":
            break
        if count == maxCount:
            break


    printGrid(distances)
    print(count)

    enclosedTiles = 0

    print("Conversion")



    def convertDots(grid, dotLocation, dotType):
        dotGrid = [dotLocation]
        tiles = ["|", "-", "L", "J", "7", "F", ".", "S"]

        # up
        while len(dotGrid) > 0:
            nextDot = dotGrid.pop()
            i = nextDot[0]
            j = nextDot[1]
            if i - 1 >= 0:
                nextDot = grid[i - 1][j]
                if nextDot == ".":
                    grid[i - 1][j] = dotType
                    dotGrid.append((i - 1, j))

            # down
            if i + 1 < len(grid):
                nextDot = grid[i + 1][j]
                if nextDot == ".":
                    grid[i + 1][j] = dotType
                    dotGrid.append((i + 1, j))
            # left
            if j - 1 >= 0:
                nextDot = grid[i][j - 1]
                if nextDot == ".":
                    grid[i][j - 1] = dotType
                    dotGrid.append((i, j - 1))

            # right
            if j + 1 < len(grid[0]):
                nextDot = grid[i][j + 1]
                if nextDot == ".":
                    grid[i][j + 1] = dotType
                    dotGrid.append((i, j + 1))

        return

    # only bother round the outside
    print("day2")

    # down the sides
    for i in range(0, len(distances)):
        convertDots(distances, (i, 0), "^")
        convertDots(distances, (i, len(distances[i]) - 1), "^")
    # across the top and bottom

    for i in range(0, len(distances[0])):
        # 0 - first line
        convertDots(distances, (0, i), "^")
        # last line
        convertDots(distances, (len(distances) - 1, i), "^")

    printGrid(distances)
    dotCount = 0
    for line in distances:
        dotCount += line.count("*")

    printGrid(distances)
    print(dotCount)



