import math
import re
import time
from functools import cmp_to_key
from day2.day2 import day2func

f = open("day9/day9test.txt", "r")
content = f.read().split("\n")
sequences = []
for line in content:
    sequences.append([int(x) for x in re.findall("[0-9]+", line)])

# print(sequences)

sequence = sequences[0]
print(sequence)


def nextSequence(sequence, addOn):
    print(sequence)
    # if last two values are 0, go back up the chain
    if len(sequence) == 1:
        return 0
    else:
        newSequence = [(sequence[i + 1] - sequence[i]) for i in range(0, len(sequence) - 1)]
        return nextSequence(newSequence, sequence[-1]) + sequence[-1]

res = 0
for sequence in sequences:
    rev = nextSequence(sequence, 0)
    print(rev)
    res += rev
# print(nextSequence(sequence, 0))
print(res)
