#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]
    bus = lines[0]
    d = lines[1].split(",")
    times = [int(x) for x in d if x != "x"]
    ntimes = [int(x) for x in range(len(d)) if d[x] != "x"]

    k = 1
    t = 0
    for i in range(len(times) - 1):
        bid = times[i+1]
        ti = ntimes[i+1]
        k *= times[i] 
        while True: 
            if (t + ti) % bid == 0:
                break
            t += k
    print(t)
