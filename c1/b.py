#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [int(line.rstrip()) for line in f]

a = set(lines)

for i in lines:
    d = 2020-i
    for p in lines:
        if d - p in a:
            print(i * (d-p) * p)
