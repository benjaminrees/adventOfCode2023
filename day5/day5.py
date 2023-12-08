import re
from collections import defaultdict

from day2.day2 import day2func

f = open("day5test.txt", "r")
# f = open("day5data.txt", "r")
content = f.read()

sections = content.split("\n\n")

seeds = list(int(x) for x in (re.findall("[0-9]+", sections[0])))
# print(seeds)

seedList = []

seedToSoil = [list(int(x) for x in re.findall("[0-9]+", line)) for line in sections[1].split("\n")[1:]]
soilToFertiliser = [list(int(x) for x in re.findall("[0-9]+", line)) for line in sections[2].split("\n")[1:]]
fertiliserToWater = [list(int(x) for x in re.findall("[0-9]+", line)) for line in sections[3].split("\n")[1:]]
waterToLight = [list(int(x) for x in re.findall("[0-9]+", line)) for line in sections[4].split("\n")[1:]]
lightToTemp = [list(int(x) for x in re.findall("[0-9]+", line)) for line in sections[5].split("\n")[1:]]
tempToHumidity = [list(int(x) for x in re.findall("[0-9]+", line)) for line in sections[6].split("\n")[1:]]
humidityToLocation = [list(int(x) for x in re.findall("[0-9]+", line)) for line in sections[7].split("\n")[1:]]

locations = []
fullResults = []

# for seed in seeds:
#     next = seed
#     result = []
#     for map in seedToSoil:
#         if map[1] <= next < (map[1] + map[2]):
#             next = map[0] + next - map[1]
#             break
#     result.append(next)
#     for map in soilToFertiliser:
#         if map[1] <= next < (map[1] + map[2]):
#             next = map[0] + next - map[1]
#             break
#     result.append(next)
#     for map in fertiliserToWater:
#         if map[1] <= next < (map[1] + map[2]):
#             next = map[0] + next - map[1]
#             break
#     result.append(next)
#     for map in waterToLight:
#         if map[1] <= next < (map[1] + map[2]):
#             next = map[0] + next - map[1]
#             break
#     result.append(next)
#     for map in lightToTemp:
#         if map[1] <= next < (map[1] + map[2]):
#             next = map[0] + next - map[1]
#             break
#     result.append(next)
#     for map in tempToHumidity:
#         if map[1] <= next < (map[1] + map[2]):
#             next = map[0] + next - map[1]
#             break
#     result.append(next)
#     for map in humidityToLocation:
#         if map[1] <= next < (map[1] + map[2]):
#             next = map[0] + next - map[1]
#             break
#     result.append(next)
#     fullResults.append(result)
#     locations.append(next)
#
# print(min(locations))

minLocation = -1

# rearrange humidity to location for lowest location
humidityToLocation.sort(key=lambda x: x[0])
# print(humidityToLocation)

# run from location 1 until we get a valid result
result = -1
next = 0
location = 0

while result == -1:
    journey = []
    next = location
    journey.append(next)

    for map in humidityToLocation:
        # if it can be mapped, pass to the next map
        if map[0] <= next < map[0] + map[2]:
            next = map[1] + next - map[0]
            break
        journey.append(next)
    for map in tempToHumidity:
        # if it can be mapped, pass to the next map
        if map[0] <= next < map[0] + map[2]:
            next = map[1] + next - map[0]
            break
        journey.append(next)
    for map in lightToTemp:
        # if it can be mapped, pass to the next map
        if map[0] <= next < map[0] + map[2]:
            next = map[1] + next - map[0]
            break
        journey.append(next)
    for map in waterToLight:
        # if it can be mapped, pass to the next map
        if map[0] <= next < map[0] + map[2]:
            next = map[1] + next - map[0]
            break
        journey.append(next)
    for map in fertiliserToWater:
        # if it can be mapped, pass to the next map
        if map[0] <= next < map[0] + map[2]:
            next = map[1] + next - map[0]
            break
        journey.append(next)
    for map in soilToFertiliser:
        # if it can be mapped, pass to the next map
        if map[0] <= next < map[0] + map[2]:
            next = map[1] + next - map[0]
            break
        journey.append(next)
    for map in seedToSoil:
        # if it can be mapped, pass to the next map
        if map[0] <= next < map[0] + map[2]:
            next = map[1] + next - map[0]
            break
        journey.append(next)

    print(journey)

    # now check if the seed number satisfies one that already exists
    for i in range(0, len(seeds), 2):
        if seeds[i] <= next <= seeds[i] + seeds[i+1] - 1:
            result = next
            print("location found")
            print(location)

    location += 1

# print(minLocation)

