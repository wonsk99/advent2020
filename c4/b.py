#!/usr/bin/env python3

valid = 0
ecls = set(["amb","blu","brn","gry","grn","hzl","oth"])
with open('./input.txt') as f:
    dCur = set()

    for line in f:
        if line.rstrip() == "":
            if len(dCur) == 7:
                valid += 1
                dCur = set()
            else:
                dCur = set()
                continue

        check = line.rstrip().split()

        for c in check:
            t, v = c.split(":")
            if t == "byr":
                if int(v) >= 1920 and int(v) <= 2002:
                    dCur.add(t)
            elif t == "iyr":
                if int(v) >= 2010 and int(v) <= 2020:
                    dCur.add(t)
            elif t == "eyr":
                if int(v) >= 2020 and int(v) <= 2030:
                    dCur.add(t)
            elif t == "hgt":
                if v[-2:] == "cm":
                    if int(v[:-2]) >= 150 and int(v[:-2]) <= 193:
                        dCur.add(t)
                if v[-2:] == "in":
                    if int(v[:-2]) >= 59 and int(v[:-2]) <= 76:
                        dCur.add(t)
            elif t == "hcl":
                if v[0] == "#":
                    if len(v[1:]) == 6 and v[1:].isalnum():
                        dCur.add(t)
            elif t == "ecl":
                if v in ecls:
                    dCur.add(t)
            elif t == "pid":
                if len(v) == 9 and v.isnumeric():
                    dCur.add(t)

    
    # Need to check last one
    if len(dCur) == 7:
        valid += 1

print(valid)
