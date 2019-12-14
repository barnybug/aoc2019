#!/usr/bin/env python

import time
import numpy as np

from intcode import Code, Executor

def part1(data):
    exe = Executor(Code(data))
    it = iter(exe.complete())
    tiles = list(zip(it, it, it))
    mx = max(x for x, _, _ in tiles) + 1
    my = max(y for _, y, _ in tiles) + 1
    board = np.zeros((my, mx))
    for x, y, i in tiles:
        board[y,x] = i
    return (board == 2).sum()

ch = {
    0: ' ',
    1: '|',
    2: '#',
    3: '~',
    4: 'O',
}

def part2(data):
    code = Code(data)
    code[0] = 2 # free play
    exe = Executor(code)
    ball = 0
    paddle = 0
    def track_ball():
        # simple strategy - paddle tracks ball
        while True:
            if ball < paddle:
                yield -1
            elif ball > paddle:
                yield 1
            else:
                yield 0

    exe.iter = track_ball()
    for x, y, t in zip(exe.runner, exe.runner, exe.runner):
        if (x, y) == (-1, 0):
            print("\033[1;45H%10d" % t)
            continue
        if t == 4:
            ball = x
        elif t == 3:
            paddle = x
        print("\033[%d;%dH%s" % (y+1, x+1, ch[t]))

    print("\033[40;0H")

if __name__ == '__main__':
    data = open('input13.txt').read()
    # print(part1(data))
    part2(data)
