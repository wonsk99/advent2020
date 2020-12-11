#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [int(line.rstrip()) for line in f]

a = set()

for i in lines:
    d = 2020-i
    if d in a:
        print(d * i)
        break
    a.add(i)
    
