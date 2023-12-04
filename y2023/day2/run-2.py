#!/home/hiyer/.asdf/shims/python

import re

num_cubes = {
        "red": 12,
        "green": 13,
        "blue": 14
        }

sum = 0

with open('day2/input.txt') as f:
    lines = f.readlines()

    for line in lines:
        line = line.strip()
        result = re.search(r"Game (?P<game_id>\d+): (?P<games>([^;]+;?)+)", line)
        # print(result.group("game_id"), result.group("games"))
        game_id = result.group("game_id")
        game = result.group("games")
        power = 1
        for color in num_cubes.keys():
            color_counts = re.findall(r"(?P<count>\d+) " + color, game)
            min_count = max([int(x) for x in color_counts])
            print(f"{color=}, {color_counts=}, {min_count=}")
            power *= min_count
        sum += power

print(sum)
