#!/usr/bin/env python

import numpy as np

def parts(data):
    a, b = map(int, data.split('-'))
    ns = np.arange(a, b)
    cols = np.array([
        (ns // (10**i)) % 10
        for i in range(5, -1, -1)
    ])
    # column-wise difference
    diffs = cols[1:] - cols[:-1]
    non_decreasing = (diffs >= 0).all(axis=0)
    repeat = (diffs == 0).any(axis=0)
    matches = repeat & non_decreasing
    part1 = (repeat & non_decreasing).sum()

    zeros = (diffs == 0)

    left = zeros[:4] & ~zeros[1:]
    right = zeros[1:] & ~zeros[:4]
    repeat = (np.pad(left, ((0,1), (0,0)), constant_values=True) &
        np.pad(right, ((1,0), (0,0)), constant_values=True))
    part2 = (repeat.any(axis=0) & non_decreasing).sum()

    return part1, part2

if __name__ == '__main__':
    part1, part2 = parts('172851-675869')
    print(part1)
    print(part2)
