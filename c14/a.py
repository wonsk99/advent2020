#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

    maskl = lines[0]
    memsl = lines[1:]

    mask = maskl.split("=")[1].strip()

    d = {}

    for mems in memsl:
        mem = ""
        i = 4
        
        if not mems[i].isnumeric():
            mask = mems.split("=")[1].strip()
            continue
        while mems[i] != "]":
            mem += mems[i]
            i += 1

        dval = int(mems.split("=")[1].strip())
        val = bin(dval).replace("0b", "")

        ex = len(mask) - len(val)
        z = "0" * ex

        val = z + val

        bit = "" 
        for i in range(len(mask)):
            if mask[i] == "X":
                bit += val[i]
            elif val[i] == "1":
                if mask[i] == "1":
                    bit += "1"
                else:
                    bit += "0"
            elif val[i] == "0":
                if mask[i] == "1":
                    bit += "1"
                else:
                    bit += "0"

        print(int(bit, 2))
        print(bit)
        print(mem)
        d[mem] = int(bit,2) 

    print(sum(d.values()))
