#!/home/hiyer/.asdf/shims/python
import re

testdata = """
Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

with open('day4/input.txt') as f:
    lines = f.readlines()
    # lines = testdata.split('\n')
    pattern = re.compile(r"Card\s+\d+:\s+(?P<winners>(\d+\s*)+)\|\s+(?P<have>(\d+\s*)+)")
    sum = 0
    for line in lines:
        line = line.strip()
        if not line:
            continue
        matches = re.search(pattern, line)
        print(line)
        winners = set([int(x) for x in re.split(r'\s+', matches.group("winners")) if x])
        have = set([int(x) for x in re.split(r'\s+', matches.group("have")) if x])
        common = winners.intersection(have)
        if common:
            sum += pow(2, len(common)-1)

print(sum)
