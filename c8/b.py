#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

me = 0
while True:
    # Accumulator
    glac = 0

    # Set
    s = set()
    
    # Index
    i = 0

    tr = 0
    while True:
        ins, ch = lines[i].split()
        ch = int(ch)

        if ins == "acc":
            glac += ch
            i += 1
        elif ins == "jmp":
            if me == tr:
                i += 1
            else:
                i += ch 
            tr += 1
        elif ins == "nop":
            if me == tr:
                i += ch
            else:
                i += 1
            tr += 1

        if i in s:
            me += 1
            break

        s.add(i)

        if i < 0 or i >= len(lines):
            print(glac)
            exit()

