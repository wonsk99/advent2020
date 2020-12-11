#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

dic = {}
for line in lines:
    c = line.split(" bags contain ")
    con = c[0].rstrip()

    d = c[1].split()
    if d[0] == "no":
        continue

    d = c[1].split(",")
    for ins in d:
        ic = " ".join(ins.split()[1:3])
        if ic not in dic:
            dic[ic] = []
        dic[ic].append(con)

print(dic)

global alrSeen

def rec(bag):
    total = 0
    if bag in alrSeen:
        return -1
    alrSeen.add(bag)
    if bag not in dic:
        return 0 
    for su in dic[bag]:
        x = rec(su)
        total += x + 1
    return total

alrSeen = set()
print(rec("shiny gold"))
