#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

cubes = {}
for l in range(len(lines)):
    for c in range(len(lines[l])):
        cubes[(l,c,0)] = lines[l][c]

around = []
for xi in range(-1,2):
    for yi in range(-1,2):
        for zi in range(-1,2):
            if xi == 0 and yi == 0 and zi == 0:
                continue
            around.append((xi,yi,zi))

for _ in range(0,6):
    ne = {}
    for cube in cubes.keys():
        # Count
        c = 0
        # Loop all directions
        for di in around:
            # A surrounding cube
            te = (cube[0]+di[0], cube[1]+di[1], cube[2]+di[2])
            if te in cubes:
                if cubes[te] == "#":
                    c += 1
            else:
                if cubes[cube] == "#":
                    c2 = 0
                    for dj in around: 
                        tk = (te[0]+dj[0],te[1]+dj[1],te[2]+dj[2])
                        if tk in cubes:
                            if cubes[tk] == "#":
                                c2 += 1
                    if c2 == 3:
                        ne[te] = "#"


        if cubes[cube] == "#":
            if c == 2 or c == 3:
                ne[cube] = "#"
            else:
                ne[cube] = "."

        else:
            if c == 3:
                ne[cube] = "#"
            else:
                ne[cube] = "."
              
    cubes = ne

total = 0
for cube in cubes.keys():
    if cubes[cube] == "#":
        total += 1
print(cubes)
print(total)
