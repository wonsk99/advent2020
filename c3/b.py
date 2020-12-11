#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

a = len(lines)
b = len(lines[0])


TOTAL = 1
dies = [(1,1),(1,3),(1,5),(1,7),(2,1)]
for die in dies:
    currs = 0
    cx = 0
    cy = 0

    m = 1

    while True:
        toTest = ""
        if cx >= b:
            m += 1

        for i in range(m):
            toTest += lines[cy]

        if toTest[cx] == "#":
            currs += 1
        cy += die[0]
        cx += die[1]
    
        if cy >= a:
            break
    TOTAL *= currs

print(TOTAL)
