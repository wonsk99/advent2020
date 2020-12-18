#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip().replace(" ", "") for line in f]

def solveLoop(i, eq):
    while eq[i] != ")":
        if eq[i].isnumeric():
            c = int(eq[i])
            i += 1
        if eq[i] == "(":
            i += 1
            i,c = solveLoop(i, eq)
        if eq[i] == "*":
            op = "*"
            i += 1
            if eq[i] == "(":
                i += 1
                i,d = solveLoop(i, eq)
                c *= d
            elif eq[i].isnumeric():
                c *= int(eq[i])
                i += 1
        elif eq[i] == "+":
            op = "+"
            i += 1
            if eq[i] == "(":
                i += 1
                i,d = solveLoop(i, eq)
                c += d
            elif eq[i].isnumeric():
                c += int(eq[i])
                i += 1
    i += 1
    return i,c

def solve(eq, total):
    i = 0
    if eq[i] == "(":
        i += 1
        i,c = solveLoop(i, eq)
        total = c
    else:
        total = int(eq[i])
        i += 1
    while i < len(eq):
        if eq[i] == "*":
            i += 1
            if eq[i] == "(":
                i += 1
                i,c = solveLoop(i, eq)
                total *= c
            elif eq[i].isnumeric():
                total *= int(eq[i])
                i += 1
        elif eq[i] == "+":
            i += 1
            if eq[i] == "(":
                i += 1
                i,c = solveLoop(i, eq)
                total += c
            elif eq[i].isnumeric():
                total += int(eq[i])
                i += 1
    return total 

running = 0
for line in lines:
    total = 0

    total = solve(line, None)

    running += total
    print(line)
    print(total)
print(running)
