#!/usr/bin/env python

import numpy as np
from intcode import Code, Executor

def intersections(output):
    lines = output.strip().split('\n')
    arr = np.array([[ord(c) for c in line] for line in lines])
    scaff = (arr == 35)
    crosses = (scaff[1:-1,:-2] & scaff[1:-1,1:-1] & scaff[1:-1,2:] & scaff[:-2,1:-1] & scaff[2:,1:-1])
    # pad border
    crosses = np.pad(crosses, ((1,1),(1,1)), constant_values=False)
    return crosses

def part1_map(output):
    inter = intersections(output)
    coords = np.argwhere(inter)
    return np.prod(coords, axis=1).sum()

def part1(data):
    exe = Executor(Code(data))
    output = ''.join(map(chr, exe.complete()))
    return part1_map(output)

def part2(data):
    code = Code(data)
    exe = Executor(code)
    output = ''.join(map(chr, exe.complete()))

    code[0] = 2
    exe = Executor(code)
    # manually devised sequence!
    main = 'A,B,A,B,A,C,B,C,A,C'
    a = 'R,4,L,10,L,10'
    b = 'L,8,R,12,R,10,R,4'
    c = 'L,8,L,8,R,10,R,4'
    live = 'n' #'y'

    for line in (main, a, b, c, live):
        exe.inputs.extend(map(ord, line))
        exe.inputs.append(10)

    for ch in exe.runner:
        if ch > 255:
            return ch
        print(chr(ch), end='')

if __name__ == '__main__':
    data = open('input17.txt').read()
    # print(part1(data))
    print(part2(data))
