#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [int(line.rstrip()) for line in f]

li = 0

d = set()

while True:
    FAIL = True
    ind = li
    tmax = li + 25

    first = lines[ind]
    d.add(first)
    ind += 1

    check = lines[tmax]

    while ind < tmax: 
        if (check - lines[ind]) in d:
            FAIL = False
            break
        d.add(lines[ind])
        ind += 1

    if FAIL:
        print(check)
        break

    li += 1

    d.remove(first)
