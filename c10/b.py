#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [int(line.rstrip()) for line in f]

jol = set(lines)
jol.add(0)

ma = max(jol)

check = 0

tab = []
tab.append(1)

for i in range(1, ma+1):
    tab.append(0)
    if i not in jol:
        continue

    if (i-3) in jol:
        tab[i] += tab[i-3]

    if (i-2) in jol:
        tab[i] += tab[i-2]

    if (i-1) in jol:
        tab[i] += tab[i-1]

print(tab)
