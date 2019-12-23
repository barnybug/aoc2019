#!/usr/bin/env python

import itertools
import numpy as np
from intcode import Code, Executor

def part1(data):
    code = Code(data)
    exe = Executor(code)
    def point(x, y):
        exe = Executor(code)
        return exe.execute(x, y)

    def search(start, end, step):
        edge = start
        for row in range(start, end, step):
            try:
                edge = next(x for x in range(edge, end, step) if point(x, row))
                yield edge
            except StopIteration:
                continue

    lefts = list(search(0, 50, 1))
    rights = list(search(49, -1, -1))
    return sum(rights) - sum(lefts) + len(lefts)

def part2(data):
    code = Code(data)
    def point(x, y):
        exe = Executor(code)
        return exe.execute(x, y)

    left = 0
    for row in itertools.count(100):
        # find left edge of this row
        left = next(x for x in itertools.count(left) if point(x, row))
        # check if top right corner is inside beam
        if point(left+99, row-99):
            return left * 10000 + (row - 99) # top left

    # incorrect: 13021155   
    return None

if __name__ == '__main__':
    data = open('input19.txt').read()
    print(part1(data))
    print(part2(data))
