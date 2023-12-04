#!/home/hiyer/.asdf/shims/python
from lib import get_first_and_last


sum = 0


def string_to_int(str):
    match str:
        case 'one' | '1':
            return 1
        case 'two' | '2':
            return 2
        case 'three' | '3':
            return 3
        case 'four' | '4':
            return 4
        case 'five' | '5':
            return 5
        case 'six' | '6':
            return 6
        case 'seven' | '7':
            return 7
        case 'eight' | '8':
            return 8
        case 'nine' | '9':
            return 9
        case 'zero' | '0':
            return 0

    return -1


strings = {'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'zero', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0'}

with open('day1/input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        line = line.strip()
        first_idx = len(line)
        first_num = last_num = None
        last_idx = -1

        for string in strings:
            first, last = get_first_and_last(string, line)
            if first is None:
                continue

            # print(f"{line=}: {first=}, {last=}")

            if first < first_idx:
                first_idx = first
                first_num = string

            if last > last_idx:
                last_idx = last
                last_num = string

        print(f"{line=}: {first_num=}, {last_num=}")
        sum += (10 * string_to_int(first_num) + string_to_int(last_num))

print(sum)
