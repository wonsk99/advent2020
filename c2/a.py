#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

TOTAL = 0
for line in lines:
    a, b, c = line.split()

    # Low and up bound
    low, high = a.split("-")
    low = int(low)
    high = int(high)

    # Letter to pay attention to
    b = b[0]

    # String
    num = 0
    for let in c:
        if let == b:
            num += 1
            if num > high:
                break
    if num >= low and num <= high:
        print(line)
        TOTAL += 1

print(TOTAL)
