#!/usr/bin/env python

from collections import deque
import numpy as np
from intcode import Code, Executor

def part1(data):
    code = Code(data)
    exe = Executor(code)
    # 0001 = 1
    # 0010 = X
    # 0011 = X
    # 0100 = X
    # 0101 = 1
    # 0110 = X
    # 0111 = 1
    # 1000 = 0
    # 1001 = 1
    # 1010 = 0
    # 1011 = 1
    # 1100 = 0
    # 1101 = 1
    # 1110 = 0
    # 1111 = 0
    # ~A | (~B & D) | (~C & D)
    lines = [
        'NOT A J',
        'NOT B T',
        'AND D T',
        'OR T J',
        'NOT C T',
        'AND D T',
        'OR T J',
        'WALK'
    ]
    for line in lines:
        exe.inputs.extend(map(ord, line))
        exe.inputs.append(10)

    for ch in exe.runner:
        if ch > 255:
            return ch
        print(chr(ch), end='')

def part2(data):
    code = Code(data)
    exe = Executor(code)
    # ABCDEFGHI
    # 0________ = 1  ~A
    # _0_______ = 1  ~B
    # ___1_____ = 1  & D
    # __0__0___ = 1  ~C & ~F
    # __0____1_ = 1  ~C & H
    lines = [
        # Jump if C and F are both holes (~C & ~F)
        'NOT C J',
        'NOT F T',
        'AND T J',

        # Jump if C is a hole and H is not a hole (~C & H)
        'NOT C T',
        'AND H T',
        'OR T J',

        # Jump if B is a hole (~B)
        'NOT B T',
        'OR T J',

        # Jump if A is a hole (~A)
        'NOT A T',
        'OR T J',

        # Walk if D is a hole (D)
        'AND D J',

        'RUN',
    ]
    for line in lines:
        exe.inputs.extend(map(ord, line))
        exe.inputs.append(10)

    for ch in exe.runner:
        if ch > 255:
            return ch
        print(chr(ch), end='')

if __name__ == '__main__':
    data = open('input21.txt').read()
    print(part1(data))
    print(part2(data))
