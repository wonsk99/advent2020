#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [list(line.rstrip()) for line in f]

rows = len(lines)
col = len(lines[0])

def checker(x):
    if x == "#":
        return True
    return False

k = 0
while True:
    occ = 0

    lchange = set()
    schange = set()

    last = [list(row) for row in lines]

    for i in range(rows):
        for j in range(col):
            seat = lines[i][j]

            # Floor
            if seat == ".":
                continue

            # Occupied
            if seat == "#":
                count = 0
                occ += 1
                
                # i-1
                if i-1 >= 0:
                    if j-1 >= 0:
                        if checker(lines[i-1][j-1]):
                            count += 1

                    if(checker(lines[i-1][j])):
                        count += 1
    
                    if j+1 < col:
                        if checker(lines[i-1][j+1]):
                            count += 1

                # i
                if j-1 >= 0:
                    if checker(lines[i][j-1]):
                        count += 1
                if j+1 < col:
                    if checker(lines[i][j+1]):
                        count += 1

                # i+1
                if i+1 < rows:
                    if j-1 >= 0:
                        if checker(lines[i+1][j-1]):
                            count += 1

                    if(checker(lines[i+1][j])):
                        count += 1
    
                    if j+1 < col:
                        if checker(lines[i+1][j+1]):
                            count += 1

                if count >= 4:
                    lchange.add((i,j))
                    occ -= 1

                continue

            if seat == "L":
                # i-1
                if i-1 >= 0:
                    if j-1 >= 0:
                        if checker(lines[i-1][j-1]):
                            continue

                    if(checker(lines[i-1][j])):
                        continue
    
                    if j+1 < col:
                        if checker(lines[i-1][j+1]):
                            continue

                # i
                if j-1 >= 0:
                    if checker(lines[i][j-1]):
                        continue
                if j+1 < col:
                    if checker(lines[i][j+1]):
                        continue

                # i+1
                if i+1 < rows:
                    if j-1 >= 0:
                        if checker(lines[i+1][j-1]):
                            continue

                    if(checker(lines[i+1][j])):
                        continue
    
                    if j+1 < col:
                        if checker(lines[i+1][j+1]):
                            continue

                schange.add((i,j))
                occ += 1
                continue
      
    for c in list(lchange):
        lines[c[0]][c[1]] = "L"

    for c in list(schange):
        lines[c[0]][c[1]] = "#"  

    if last == lines:
        print(occ)
        break
    else:
        last = [list(row) for row in lines]

