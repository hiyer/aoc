#!/home/hiyer/.asdf/shims/python
from collections import defaultdict
import re

testlines = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def get_adjacent_slots(row, col):
    for i in range(row - 1, row + 2):
        for j in range(col - 1, col + 2):
            if i == row and j == col:
                continue
            yield (i, j)


symbols = set("*=%#@$&+\/-")


class PartNumber:

    def __init__(self, num):
        self._num = num

    def zero(self):
        self._num = 0

    def value(self):
        return self._num


matrix = defaultdict(lambda: defaultdict(PartNumber))


with open('day3/input.txt', 'r') as f:
    # lines = testlines.split('\n')  
    lines = f.readlines()
    pattern = re.compile(r"(?P<dots>\.+)|(?P<number>\d+)|(?P<symbol>[*=%#@$&+\/-])")
    row = 0
    for line in lines:
        if not line:
            continue
        col = 0
        line = line.strip()
        for match in re.finditer(pattern, line):
            if dots := match.group("dots"):
                col += len(dots)
            elif num := match.group("number"):
                part_num = PartNumber(int(num))
                for c in range(len(num)):
                    matrix[row][col + c] = part_num
                col += len(num)
            elif symbol := match.group("symbol"):
                matrix[row][col] = symbol
                col += 1
            else:
                print(f"No matches on line {line}")
        row += 1

sum = 0
for k1, v1 in matrix.items():
    for k2, v2 in v1.items():
        # print(f"{k1=}, {k2=}, {v2=}")
        if v2 in symbols:
            for (row, col) in get_adjacent_slots(k1, k2):
                print(f"{v2=}, {row=}, {col=}")
                if elem := matrix.get(row, {}).get(col, None):
                    if isinstance(elem, PartNumber):
                        sum += elem.value()
                        elem.zero()
                        print(f"{sum=}")
print(sum)
