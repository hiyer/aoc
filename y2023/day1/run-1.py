#!/home/hiyer/.asdf/shims/python

sum = 0
with open('input.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        digits = list(filter(lambda x: x.isdigit(), line))
        if len(digits) > 1:
            first, *_, last = digits
            sum += (10*int(first) + int(last))
        elif len(digits) == 1:
            sum += (11*int(digits[0]))

print(sum)
