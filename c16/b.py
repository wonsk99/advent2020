#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]

pre = True
your = True

d = {}
pos = {}

my = []
alltix = []

values = set()

for p in lines:
    if pre:
        if p == "":
            pre = False
        else:
            temp = p.split(":")
            typ = temp[0].strip()
            vals = temp[1].strip()
            pos[typ] = set()
            v1, v2 = vals.split(" or ") 
            d[typ] = set()
            for i in range(int(v1.split("-")[0]), int(v1.split("-")[1]) + 1): 
                d[typ].add(i)
                values.add(i)
            for i in range(int(v2.split("-")[0]), int(v2.split("-")[1]) + 1): 
                d[typ].add(i)
                values.add(i)
    elif your:
        if p == "":
            your = False
            continue
        elif p[0] == "y":
            continue
        else:
            ml = p.split(",")
            for i in ml:
                my.append(int(i))
            alltix.append(my)
    else:
        if p == "":
            continue
        elif p[0] == "n":
            continue
        else:
            tic = []
            for i in p.split(","):
                if int(i) not in values:
                    t = False
                    break
                else:
                    tic.append(int(i)) 
            if len(tic) == len(my):
                alltix.append(tic)

for name in d.keys():
    for loc in range(len(my)):
        f = True
        for ti in alltix:
            if ti[loc] not in d[name]:
                f = False
                break
        if f:
            pos[name].add(loc)

deps = []

while pos:
    for lo in pos.keys():
        if len(pos[lo]) == 1:
            af = pos[lo].pop()
            if "departure" in lo:
                deps.append(af) 
            del pos[lo]
            for ol in pos.keys():
                if af in pos[ol]:
                    pos[ol].remove(af)
            break

ff = 1
for i in deps:
    ff *= my[i]
print(ff)
