#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

    maskl = lines[0]
    memsl = lines[1:]

    mask = maskl.split("=")[1].strip()

    d = {}

    for mems in memsl:
        # Memory address in decimal
        mem = ""

        i = 4
        
        if not mems[i].isnumeric():
            mask = mems.split("=")[1].strip()
            continue
        while mems[i] != "]":
            mem += mems[i]
            i += 1

        # Memory address in binary
        bmem = bin(int(mem)).replace("0b", "")

        # Find "X"ed address
        bitmem = ""
        # Number of extra zeros to match length of mask
        memex = len(mask) - len(bmem)
        # Where are the X
        xi = []
        # Memory addresses to write to in binary
        adds = []

        bmem = "0"*memex + bmem

        for i in range(len(mask)):
            if mask[i] == "X":
                bitmem += "X"
                xi.append(i)
            elif bmem[i] == "1" or mask[i] == "1":
                bitmem += "1"
            else:
                bitmem += "0"

        adds.append(bitmem)

        while len(xi) > 0:
            temad = []
            pos = xi.pop()
            for x in adds:
                temad.append(x[0:pos] + "0" + x[pos+1:])
                temad.append(x[0:pos] + "1" + x[pos+1:])
                
            adds = list(temad)

        # Value in decimal
        dval = int(mems.split("=")[1].strip())

        for add in adds:
            tow = int(add, 2)
            d[tow] = dval 

    print(sum(d.values()))
