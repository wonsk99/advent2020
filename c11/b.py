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

                t0=1
                t1=1
                t2=1

                t3=1
                t4=1

                t5=1
                t6=1
                t7=1

                # AAA
                # i-1, j-1
                while i-t0 >= 0 and j-t0 >= 0:
                    if lines[i-t0][j-t0] != "L":
                        if lines[i-t0][j-t0] == "#":
                            print("A")
                            count += 1
                            break
                    else:
                        break
                    t0 += 1        

                # i-1, j
                while i-t1 >= 0:
                    if lines[i-t1][j] != "L":
                        if lines[i-t1][j] == "#":
                            print("B")
                            count += 1
                            break
                    else:
                        break
                    t1 += 1
                # i-1, j+1
                while i-t2 >= 0 and j+t2 < col: 
                    if lines[i-t2][j+t2] != "L":
                        if lines[i-t2][j+t2] == "#":
                            print("C")
                            count += 1
                            break
                    else:
                        break
                    t2 += 1

                # BBB
                # i, j-1
                while j-t3 >= 0:
                    if lines[i][j-t3] != "L":
                        if lines[i][j-t3] == "#":
                            print("D")
                            count += 1               
                            break
                    else:
                        break
                    t3 += 1

                # i, j+1
                while j+t4 < col:
                    if lines[i][j+t4] != "L":
                        if lines[i][j+t4] == "#":
                            print("E")
                            count += 1               
                            break
                    else:
                        break
                    t4 += 1

                # CCC
                # i+1, j-1
                while i+t5 < rows and j-t5 >= 0:
                    if lines[i+t5][j-t5] != "L":
                        if lines[i+t5][j-t5] == "#":
                            print("F")
                            count += 1
                            break
                    else:
                        break
                    t5 += 1

                # i+1, j
                while i+t6 < rows:
                    if lines[i+t6][j] != "L":
                        if lines[i+t6][j] == "#":
                            print("G")
                            count += 1
                            break
                    else:
                        break
                    t6 += 1

                # i+1, j+1
                while i+t7 < rows and j+t7 < col:
                    if lines[i+t7][j+t7] != "L":
                        if lines[i+t7][j+t7] == "#":
                            print("H")
                            count += 1
                            break
                    else:
                        break
                    t7 += 1

                if count >= 5:
                    print(i,j, count)
                    lchange.add((i,j))
                    occ -= 1

                continue


                
            if seat == "L":
                track = False
                t0=1
                t1=1
                t2=1

                t3=1
                t4=1

                t5=1
                t6=1
                t7=1

                # AAA
                # i-1, j-1
                while i-t0 >= 0 and j-t0 >= 0:
                    if lines[i-t0][j-t0] != "L":
                        if lines[i-t0][j-t0] == "#":
                            print("1")
                            track = True
                            break
                    else:
                        break         
                    t0 += 1        
                if track:
                    continue

                # i-1, j
                while i-t1 >= 0:
                    if lines[i-t1][j] != "L":
                        if lines[i-t1][j] == "#":
                            print("2")
                            track = True
                            break
                    else:
                        break         
                    t1 += 1
                if track:
                    continue
                # i-1, j+1
                while i-t2 >= 0 and j+t2 < col: 
                    if lines[i-t2][j+t2] != "L":
                        if lines[i-t2][j+t2] == "#":
                            print("3")
                            track = True
                            break
                    else:
                        break         
                    t2 += 1
                if track:
                    continue

                # BBB
                # i, j-1
                while j-t3 >= 0:
                    if lines[i][j-t3] != "L":
                        if lines[i][j-t3] == "#":
                            print("4")
                            track = True
                            break
                    else:
                        break         
                    t3 += 1
                if track:
                    continue

                # i, j+1
                while j+t4 < col:
                    if lines[i][j+t4] != "L":
                        if lines[i][j+t4] == "#":
                            print("5")
                            track = True
                            break
                    else:
                        break         
                    t4 += 1
                if track:
                    continue

                # CCC
                # i+1, j-1
                while i+t5 < rows and j-t5 >= 0:
                    if lines[i+t5][j-t5] != "L":
                        if lines[i+t5][j-t5] == "#":
                            print("6")
                            track = True
                            break
                    else:
                        break         
                    t5 += 1
                if track:
                    continue

                # i+1, j
                while i+t6 < rows:
                    if lines[i+t6][j] != "L":
                        if lines[i+t6][j] == "#":
                            print("7")
                            track = True
                            count += 1
                            break
                    else:
                        break         
                    t6 += 1
                if track:
                    continue

                # i+1, j+1
                while i+t7 < rows and j+t7 < col:
                    if lines[i+t7][j+t7] != "L":
                        if lines[i+t7][j+t7] == "#":
                            print("8")
                            track = True
                            break
                    else:
                        break         
                    t7 += 1
                if track:
                    continue

                schange.add((i,j))
                occ += 1
                continue
    
    for c in list(lchange):
        lines[c[0]][c[1]] = "L"

    for c in list(schange):
        lines[c[0]][c[1]] = "#"

    print(k)
    for i in lines:
        print(i)   
    print("----------------")         
    for i in last:
        print(i)   
    print("----------------")         

    if last == lines:
        print(occ)
        break
    else:
        last = [list(row) for row in lines]

    k+= 1
