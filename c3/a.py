#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

cx = 0
cy = 0
a = len(lines)
b = len(lines[0])

m = 1

TOTAL = 0
while True:
    toTest = ""
    if cx > b:
        m += 1

    for i in range(m):
        toTest += lines[cy]

    if toTest[cx] == "#":
        TOTAL += 1
    cy += 1
    cx += 3
    
    if cy == a:
        break

print(TOTAL)
