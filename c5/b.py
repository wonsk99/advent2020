#!/usr/bin/env python3
import math

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

prevs = set()
poss = set()

for line in lines:
    lb = 0
    rb = 127
    for ch in line[:7]:
        if ch == "F":
            rb = math.floor((rb+lb)/2)
        if ch == "B":
            lb = math.ceil((rb+lb)/2)
    row = lb

    lb = 0
    rb = 7
    for ch in line[7:]:
        if ch == "L":
            rb = math.floor((rb+lb)/2)
        if ch == "R":
            lb = math.ceil((rb+lb)/2)
    col = lb

    fid = row * 8 + col
    if fid - 2 in prevs:
        if fid - 1 not in prevs:
            poss.add(fid-1)
    elif fid + 2 in prevs:
        if fid - 1 not in prevs:
            poss.add(fid+1)

    prevs.add(fid)

for i in poss:
    if i not in prevs:
        print(i)
        break

