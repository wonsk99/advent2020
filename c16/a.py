#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

pre = True
your = True

values = set()
my = []

rate = 0

for p in lines:
    if pre:
        if p == "":
            pre = False
        else:
            vals = p.split(":")[1].strip()
            v1, v2 = vals.split(" or ") 
            for i in range(int(v1.split("-")[0]), int(v1.split("-")[1]) + 1): 
                values.add(i)
            for i in range(int(v2.split("-")[0]), int(v2.split("-")[1]) + 1): 
                values.add(i)
    elif your:
        if p == "":
            your = False
            continue
        elif p[0] == "y":
            continue
        else:
            my = p.split(",")
    else:
        if p == "":
            continue
        elif p[0] == "n":
            continue
        else:
            for i in p.split(","):
                if int(i) not in values:
                    rate += int(i)

print(rate)
