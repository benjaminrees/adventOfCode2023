import re
from collections import defaultdict

from day2.day2 import day2func

f = open("day5test.txt", "r")
# f = open("day5data.txt", "r")
content = f.read()

sections = content.split("\n\n")

