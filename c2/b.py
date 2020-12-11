#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

TOTAL = 0
for line in lines:
    a, b, c = line.split()

    # Indices
    low, high = a.split("-")
    low = int(low)
    high = int(high)

    # Letter to pay attention to
    b = b[0]

    # String
    x = 0
    if c[low-1] == b:
        x += 1
    if c[high-1] == b:
        x += 1
    if x == 1:
        TOTAL += 1

print(TOTAL)
