#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

TOTAL = 0
yes = set()
first = True

for line in lines:
    if line == "":
        TOTAL += len(yes)
        yes = set()
        first = True
        continue

    temp = []
    for ch in line:
        if len(yes) == 0:
            if first:
                temp.append(ch)
        if ch in yes:
            temp.append(ch)
    if first:
        first = False

    yes = set(temp)

TOTAL += len(yes)
print(TOTAL)
