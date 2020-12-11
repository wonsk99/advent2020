#!/usr/bin/env python3

'''
89084 bags are in a 'shiny gold.'
'''

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
        if con not in dic:
            dic[con] = []
        dic[con].append((ic, int(ins.split()[0])))

def rec(bag):
    total = 0
    if bag not in dic:
        return 0
    for bg in dic[bag]:
        total += bg[1] + bg[1] * rec(bg[0])

    return total

print(dic["shiny gold"])
print(rec("shiny gold"))
