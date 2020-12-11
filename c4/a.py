#!/usr/bin/env python3

valid = 0
with open('./input.txt') as f:
    dAll = set()
    dAll.add("byr")
    dAll.add("iyr")
    dAll.add("eyr")
    dAll.add("hgt")
    dAll.add("hcl")
    dAll.add("ecl")
    dAll.add("pid")
    # dAll.add("cid")

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
            if c[:3] in dAll:
                dCur.add(c[:3])

    
    # Need to check last one
    if len(dCur) == 7:
        valid += 1

print(valid)
