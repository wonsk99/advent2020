#!/usr/bin/env python3

inp = [2,0,1,9,5,19]

d = {}

turn = 1
for i in inp:
    d[i] = turn
    turn += 1
    last = i

last = 0

for turn in range(len(inp)+2, 30000001):
    if last in d:
        nextl = turn - 1 - d[last]
        d[last] = turn - 1
        last = nextl
    else:
        d[last] = turn - 1
        last = 0
    print(turn, last)
