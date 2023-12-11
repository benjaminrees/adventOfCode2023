import math
import re
import time
from functools import cmp_to_key
from day2.day2 import day2func

f = open("day9/day9data.txt", "r")
content = f.read().split("\n")
sequences = []
for line in content:
    sequences.append([int(n) for n in line.split()])

# def nextSequence(sequence):
#     print(sequence)
#     # if last two values are 0, go back up the chain
#     if len(sequence) == 1:
#         return 0
#     else:
#         newSequence = [sequence[i + 1] - sequence[i] for i in range(0, len(sequence) - 1)]
#         return nextSequence(newSequence) + sequence[-1]
#
# res = 0
# for sequence in sequences:
#     rev = nextSequence(sequence)
#     print(rev)
#     res += rev
# # print(nextSequence(sequence, 0))
# print(res)

def nextSequence(sequence):
    print(sequence)
    # if last two values are 0, go back up the chain
    if all(y == 0 for y in sequence):
        return 0
    else:
        newSequence = [sequence[i + 1] - sequence[i] for i in range(0, len(sequence) - 1)]
        return sequence[0] - nextSequence(newSequence)



test = [10, 13, 16, 21, 30, 45]

print(nextSequence(test))

res = 0
for sequence in sequences:
    rev = nextSequence(sequence)
    print(rev)
    res += rev
# print(nextSequence(sequence, 0))
print(res)