#!/usr/bin/env python

import numpy as np
from util import loadints

def part1(data):
    return (loadints(data) // 3 - 2).sum()

def positives(n):
    return n[n > 0]

def fuelseq(n):
    while (n := positives(n//3-2)).size:
        yield n.sum()

def part2(data):
    n = loadints(data)
    return sum(i for i in fuelseq(n))

if __name__ == '__main__':
    print(part1('input01.txt'))
    print(part2('input01.txt'))
