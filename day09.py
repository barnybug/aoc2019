#!/usr/bin/env python

import numpy as np

from intcode import Code, Executor

def part1(code):
    return Executor(code).complete(1)

def part2(code):
    return Executor(code).complete(2)

if __name__ == '__main__':
    code = Code(open('input09.txt').read())
    print(part1(code))
    print(part2(code))
