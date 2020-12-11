#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

# Accumulator
glac = 0

# Set
s = set()

# Index
i = 0

while True:
    ins, ch = lines[i].split()
    ch = int(ch)

    if ins == "acc":
        glac += ch
        i += 1
    elif ins == "jmp":
        i += ch 
    elif ins == "nop":
        i += 1

    if i in s:
        print(glac)
        break
    s.add(i)

    

    
    
