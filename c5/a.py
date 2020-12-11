#!/usr/bin/env python3
import math

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

maxID = 0

for line in lines:
    lb = 0
    rb = 127
    for ch in line[:7]:
        if ch == "F":
            rb = math.floor((rb+lb)/2)
            print(lb,rb)
        if ch == "B":
            lb = math.ceil((rb+lb)/2)
            print(lb,rb)
    row = lb

    lb = 0
    rb = 7
    for ch in line[7:]:
        if ch == "L":
            rb = math.floor((rb+lb)/2)
            print(lb,rb)
        if ch == "R":
            lb = math.ceil((rb+lb)/2)
            print(lb,rb)
    col = lb

    maxID = max(maxID, row * 8 + col)

print(maxID)
