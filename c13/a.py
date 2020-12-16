#!/usr/bin/env python3

with open('./input.txt') as f:
    lines = [line.rstrip() for line in f]
    bus = lines[0]
    times = [int(x) for x in lines[1].split(",") if x.isnumeric()]
    
    i = int(bus)

    while True:
        for time in times:
            if i % time == 0:
                print((i-int(bus)) * time)
                exit()

        i += 1
