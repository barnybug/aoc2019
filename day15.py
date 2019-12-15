#!/usr/bin/env python

import time
from dataclasses import dataclass

import numpy as np
from intcode import Code, Executor

@dataclass
class Point:
    x: int
    y: int
    walk: list

dx = [0, 0, 0, -1, 1]
dy = [0, -1, 1, 0, 0]
rev = [0, 2, 1, 4, 3]

def draw(x, y, c):
    print("\033[%d;%dH%s\033[47;1H" % (y+23, x+23, c))

def prefix(l1, l2):
    for i, (a, b) in enumerate(zip(l1, l2)):
        if a != b:
            return i
    return min(len(l1), len(l2))

def walk(data):
    exe = Executor(Code(data))
    grid = {}
    queue = [Point(0, 0, [])]
    draw(0, 0, '.')
    breadth = True
    while True:
        p = queue.pop(0)
        # check each direction
        for i in (1, 2, 3, 4):
            nx = p.x + dx[i]
            ny = p.y + dy[i]
            if (nx, ny) in grid:
                continue
            # try this direction
            resp = exe.execute(i)
            assert resp in (0, 1, 2)
            if resp == 0:
                # wall, unchanged
                grid[nx, ny] = '#'
                draw(nx, ny, '#')
            elif resp in (1, 2):
                if resp == 2:
                    part1 = len(p.walk)+1
                    breadth = False
                c = '.' if resp == 1 else 'O'
                grid[nx, ny] = c
                draw(nx, ny, c)
                # moved - add to explore list
                if resp == 1:
                    # Odd, if you explore from the oxygen we get an 
                    # assertion failure (ie position is off).
                    if breadth:
                        queue.append(Point(nx, ny, p.walk + [i]))
                    else:
                        queue.insert(0, Point(nx, ny, p.walk + [i]))
                # retrace step
                assert exe.execute(rev[i]) == 1
        
        if not queue:
            break

        # optimisation: return to common point in next point
        np = queue[0]
        i = prefix(np.walk, p.walk)
        for j in reversed(p.walk[i:]):
            assert exe.execute(rev[j]) == 1
        for j in np.walk[i:]:
            assert exe.execute(j) == 1

    return part1, grid

@dataclass
class Oxygen:
    x: int
    y: int
    time: int

def fill(grid):
    queue = [Oxygen(x, y, 0) for (x, y), c in grid.items() if c == 'O']
    while queue:
        p = queue.pop(0)
        for i in (1, 2, 3, 4):
            nx = p.x + dx[i]
            ny = p.y + dy[i]
            if grid.get((nx, ny)) == '.':
                grid[nx, ny] = 'O'
                draw(nx, ny, 'O')
                queue.append(Oxygen(nx, ny, p.time + 1))
                time.sleep(0.002) # animate

        if not queue:
            return p.time

def parts(data):
    part1, grid = walk(data)
    print("\033[%d;%dHpart1: %s" % (45, 1, part1))
    part2 = fill(grid)
    print("\033[%d;%dHpart2: %s" % (46, 1, part2))
    
if __name__ == '__main__':
    data = open('input15.txt').read()
    parts(data)
