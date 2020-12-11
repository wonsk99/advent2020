#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [int(line.rstrip()) for line in f]

jol = set(lines)

check = 0

one = 0
three = 1

for i in lines:
    if (check + 1) in jol:
        one += 1
        jol.remove(check + 1)
        check += 1
    elif (check + 2) in jol:
        jol.remove(check + 2)
        check += 2
    elif (check + 3) in jol:
        three += 1
        jol.remove(check + 3)
        check += 3
    print(check)

print(one * three)
