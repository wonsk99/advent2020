#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

# Waypoint
e = 10
n = 1

# Ship
loce = 0
locn = 0
    
for move in lines:
    dire = move[0]
    val = int(move[1:])

    if dire == "N":
        n += val
    elif dire == "S":
        n -= val
    elif dire == "E":
        e += val
    elif dire == "W":
        e -= val
    elif dire == "L" or dire == "R":
        # Left
        if dire == "R":
            # 90
            if val == 90:
                t = n
                n = -e
                e = t 
            # 180
            if val == 180:
                n = -n
                e = -e
            # 270
            if val == 270:
                t = n
                n = e
                e = -t 

        # R
        if dire == "L":
            # 90
            if val == 90:
                t = n
                n = e
                e = -t 
            # 180
            if val == 180:
                n = -n
                e = -e
            # 270
            if val == 270:
                t = n
                n = -e
                e = t 

    elif dire == "F":
        loce += e*val
        locn += n*val

    print(loce, locn)
    print(abs(loce) + abs(locn))
