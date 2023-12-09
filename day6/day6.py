f = open("day6data.txt", "r")
content = f.read().split("\n")



times = content[0].split()[1:]
distances = content[1].split()[1:]

recordTime = 7
recordDistance = 9
results = []

# res = 1
# for i in range(0, len(distances), 1):
#     results = []
#     for buttonTime in range(1, int(times[i]), 1):
#         distance = buttonTime * (int(times[i]) - buttonTime)
#         if distance >= int(distances[i]):
#             results.append(buttonTime)
#     res *= len(results)

res = 1

time = int("".join(times))
targetDistance = int("".join(distances))

for buttonTime in range(1, time, 1):
    distance = buttonTime * (time - buttonTime)
    if distance > targetDistance:
        results.append(buttonTime)

res = len(results)

# print(results)
print(res)