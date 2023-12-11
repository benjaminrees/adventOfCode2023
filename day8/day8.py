f = open("day8data.txt", "r")
content = f.read().split("\n")

directions = content[0]
nodes = {}

for line in content[2:]:
    x = [x for x in re.findall("[A-Z0-9]+", line)]
    nodes[x[0]] = (x[1], x[2])

print(nodes)


def getNextNode(elem, index):
    if directions[index] == "L":
        return nodes[elem][0]
    else:
        return nodes[elem][1]


# element = "AAA"
# steps = 0
# i = 0
# while element != "ZZZ":
#     element = getNextNode(element, i)
#
#     steps += 1
#     i += 1
#     if i == 263:
#         i = 0
# print(steps)

startNodes = [a for a in nodes.keys() if a[2] == "A"]
endNodes = [a for a in nodes.keys() if a[2] == "Z"]

steps = 0
dirIndex = 0
finished = False
result = []

print("Start nodes")
print(startNodes)
print("End nodes")
print(endNodes)
currentNode = startNodes

# while not finished:
#     for j in range(0, len(currentNode)):
#         currentNode[j] = getNextNode(currentNode[j], dirIndex)
#         if currentNode[j][2] == "Z":
#             print(currentNode[j])
#
#     # time.sleep(1)
#     # print(directions[dirIndex])
#     # print(currentNode)
#
#     steps += 1
#     dirIndex += 1
#     if dirIndex == len(directions):
#         dirIndex = 0
#
#     if all([x[2] == "Z" for x in currentNode]):
#         finished = True


stepsRequired = []
for k in range(0, len(startNodes)):
    steps = 1
    dirIndex = 0
    finished = False
    currentNode = startNodes[k]
    nodesVisited = []

    while not finished:
        currentNode = getNextNode(currentNode, dirIndex)
        if currentNode[2] == "Z":
            finished = True
            stepsRequired.append(steps)


        steps += 1
        dirIndex += 1
        if dirIndex == len(directions):
            dirIndex = 0

print(stepsRequired)

print(math.lcm(*stepsRequired))