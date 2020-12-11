#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

TOTAL = 0
yes = set()

for line in lines:
    if line == "":
        TOTAL += len(yes)
        yes = set()
    for ch in line:
        yes.add(ch)

TOTAL += len(yes)
print(TOTAL)
