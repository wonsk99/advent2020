#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [int(line.rstrip()) for line in f]

myNum = 3199139634

li = 0

while True:
    theSum = 0
    ind = li

    maxA = 0
    minA = myNum + 1

    while True:
        if lines[ind] > maxA:
            maxA = lines[ind]
        if lines[ind] < minA:
            minA = lines[ind]

        theSum += lines[ind] 
         
        if theSum == myNum:
            print(maxA + minA)
            exit()

        if theSum > myNum:
            break

        ind += 1

    li += 1
