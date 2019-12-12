#!/usr/bin/env python

import numpy as np
from intcode import Code, Executor

def robot(exe, initial=0):
    pos = (0, 0)
    step = (0, -1)
    grid = {}
    exe.inputs = [initial]
    for colour, move in zip(exe.runner, exe.runner):
        grid[pos] = colour
        if move == 0: # left
            step = (step[1], -step[0])
        else:
            step = (-step[1], step[0])
        pos = (pos[0]+step[0], pos[1]+step[1])
        exe.inputs = [grid.get(pos, 0)]
    return grid

def part1(data):
    return len(robot(Executor(code)))

def part2(data):
    grid = robot(Executor(code), initial=1)
    paint = np.array([(pos[1], pos[0]) for pos, colour in grid.items() if colour])
    size = paint.max(axis=0) + [1, 1]
    panel = np.full(size, '.')
    panel[paint[:,0],paint[:,1]] = '#'
    return '\n'.join(''.join(row) for row in panel)

if __name__ == '__main__':
    code = Code(open('input11.txt'))
    print(part1(code))
    print(part2(code))
