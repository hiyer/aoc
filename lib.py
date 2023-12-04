#!/home/hiyer/.asdf/shims/python

def findall(substring, string):
    i = string.find(substring)
    while i != -1:
        yield i
        i = string.find(substring, i+1)


def get_first_and_last(substring, string):
    first = last = None
    occurrences = list(findall(substring, string))
    # print(f"{substring=}, {string=}, {occurrences=}")
    if len(occurrences) > 1:
        first, *_, last = occurrences
    elif len(occurrences) == 1:
        first = last = occurrences[0]

    return first, last
