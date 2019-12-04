#!/usr/bin/env python

import numpy as np
from util import loadints
from collections import defaultdict

dirs = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

def tracepath(path):
    board = {}
    x, y = (0, 0)
    steps = 0
    for step in path.split(','):
        n = int(step[1:])
        dx, dy = dirs[step[0]]
        for _ in range(0, n):
            steps += 1
            x += dx
            y += dy
            if (x, y) not in board:
                board[x,y] = steps

    return board

def tracepaths(data):
    path1, path2 = list(data)
    b1 = tracepath(path1)
    b2 = tracepath(path2)
    return b1, b2

def part1(data):
    b1, b2 = tracepaths(data)
    crosses = b1.keys() & b2.keys()
    manhattan = [abs(x)+abs(y) for x, y in crosses]
    closest = min(manhattan)
    return closest

def part2(data):
    b1, b2 = tracepaths(data)
    crosses = b1.keys() & b2.keys()
    delays = [b1[c] + b2[c] for c in crosses]
    return min(delays)

if __name__ == '__main__':
    print(part1(open('input03.txt')))
    print(part2(open('input03.txt')))
