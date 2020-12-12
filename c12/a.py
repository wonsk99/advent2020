#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

e = 0
n = 0
    
curr = "E"

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
        if dire == "L":
            # 90
            if val == 90:
                if curr == "N":
                    curr = "W"
                elif curr == "W":
                    curr = "S"
                elif curr == "S":
                    curr = "E"
                elif curr == "E":
                    curr = "N"
            # 180
            if val == 180:
                if curr == "N":
                    curr = "S"
                elif curr == "W":
                    curr = "E"
                elif curr == "S":
                    curr = "N"
                elif curr == "E":
                    curr = "W"
            # 270
            if val == 270:
                if curr == "N":
                    curr = "E"
                elif curr == "E":
                    curr = "S"
                elif curr == "S":
                    curr = "W"
                elif curr == "W":
                    curr = "N"

        # R
        if dire == "R":
            # 90
            if val == 90:
                if curr == "N":
                    curr = "E"
                elif curr == "E":
                    curr = "S"
                elif curr == "S":
                    curr = "W"
                elif curr == "W":
                    curr = "N"
            # 180
            if val == 180:
                if curr == "N":
                    curr = "S"
                elif curr == "W":
                    curr = "E"
                elif curr == "S":
                    curr = "N"
                elif curr == "E":
                    curr = "W"
            # 270
            if val == 270:
                if curr == "N":
                    curr = "W"
                elif curr == "W":
                    curr = "S"
                elif curr == "S":
                    curr = "E"
                elif curr == "E":
                    curr = "N"

    elif dire == "F":
        if curr == "N":
            n += val
        elif curr == "E":
            e += val
        elif curr == "S":
            n -= val
        elif curr == "W":
            e -= val

    print(e,n)
    print(abs(e) + abs(n))
