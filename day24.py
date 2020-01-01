#!/usr/bin/env python

import numpy as np

def parse(data):
    c = np.array([list(line) for line in data.split()])
    return c == '#'

powers = [2**i for i in range(25)]

def rating(grid):
    return (grid.flatten() * powers).sum()

def surrounding(y, x):
    s = np.zeros((5, 5), bool)
    if x > 0:
        s[y,x-1] = True
    if x < 4:
        s[y,x+1] = True
    if y > 0:
        s[y-1,x] = True
    if y < 4:
        s[y+1,x] = True
    return s

def part1(data):
    c = np.array([list(line) for line in data.split()])
    grid = (c == '#')
    seen = set()

    masks = [
        [
            surrounding(y, x)
            for x in range(5)
        ]
        for y in range(5)
    ]
    while True:
        r = rating(grid)
        if r in seen:
            return r
        seen.add(r)

        counts = np.zeros(grid.shape)
        for y in range(5):
            for x in range(5):
                counts[y,x] = (grid & masks[y][x]).sum()

        grid = (counts == 1) | (~grid & (counts == 2))

def surrounding3d(y, x):
    a = np.zeros((5, 5), bool) # above
    s = np.zeros((5, 5), bool) # same
    b = np.zeros((5, 5), bool) # below

    if x == 1 and y == 2:
        s[2,0] = True
        b[:,0] = True
    elif x == 3 and y == 2:
        s[2,4] = True
        b[:,4] = True
    else:
        if x == 0:
            a[2,1] = True
        else:
            s[y,x-1] = True
        if x == 4:
            a[2,3] = True
        else:
            s[y,x+1] = True

    if y == 1 and x == 2:
        s[0,2] = True
        b[0,:] = True
    elif y == 3 and x == 2:
        s[4,2] = True
        b[4,:] = True
    else:
        if y == 0:
            a[1,2] = True
        else:
            s[y-1,x] = True
        if y == 4:
            a[3,2] = True
        else:
            s[y+1,x] = True

    return a, s, b

def part2(data, minutes):
    c = np.array([list(line) for line in data.split()])
    grids = [(c == '#')]
    masks = [
        [
            surrounding3d(y, x)
            for x in range(5)
        ]
        for y in range(5)
    ]
    for i in range(minutes):
        if grids[-1].sum():
            # add blank above
            grids.append(np.zeros((5,5), bool))
        if grids[0].sum():
            # add blank below
            grids.insert(0, np.zeros((5,5), bool))
        
        newgrids = []
        for z, grid in enumerate(grids):
            counts = np.zeros(grid.shape)
            for y in range(5):
                for x in range(5):
                    if x == y == 2:
                        continue
                    a, s, b = masks[y][x]
                    counts[y,x] = (grid & s).sum()
                    if z > 0:
                        counts[y,x] += (grids[z-1] & b).sum() # below
                    if z < len(grids)-1: #
                        counts[y,x] += (grids[z+1] & a).sum() # above

            grid = (counts == 1) | (~grid & (counts == 2))
            newgrids.append(grid)
        
        grids = newgrids
        
    # for z, grid in enumerate(grids):
    #     print(z, grid)

    return sum(grid.sum() for grid in grids)

if __name__ == '__main__':
    data = open('input24.txt').read()
    # print(part1(data))
    print(part2(data, 200))
