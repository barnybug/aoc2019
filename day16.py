#!/usr/bin/env python

import numpy as np
import math
from tqdm import tqdm

def patterns(size):
    for i in range(size):
        base = np.repeat(np.array([0, 1, 0, -1]), i+1)
        pattern = np.tile(base, math.ceil((size+1)/len(base)))
        yield pattern[1:size+1]

def part1(data, phases):
    signal = np.array(list(data), dtype=int)
    size = len(signal)
    matrix = np.array(list(patterns(size)))
    for phase in range(phases):
        i = signal * matrix
        signal = np.abs(i.sum(axis=1)) % 10
    return ''.join(map(str, signal))

def part2(data, phases):
    unit = np.array(list(data), dtype=int)
    offset = int(data[:7])
    # This method assumes the offset is over halfway along the array
    # ie. we can just calculate with sums
    assert offset >= (len(unit) * 10000)/2
    size = len(unit) * 10000 - offset
    # We don't need to consider the part of the signal prior to the offset,
    # so use a partial signal from this point onwards.
    signal = np.tile(unit, math.ceil(size/len(unit)))[-size:]

    # We need to calculate the triangular sum:
    # [1 1 1 1 1]
    # [0 1 1 1 1]
    # [0 0 1 1 1]
    # ...
    # Which is actually just cumsum from the far end backwards, so
    # instead first reverse the signal, then use cumsum.
    # Each phase is then just this cumsum step repeated. Nice and quick.
    rsignal = signal[::-1]
    for phase in tqdm(range(phases)):
        rsignal = np.cumsum(rsignal) % 10
    
    # Answer is the first 8 digits of the signal.
    # So undo the reverse of the signal
    signal = rsignal[::-1]
    # Then take the first 8
    return ''.join(map(str, signal[:8]))

if __name__ == '__main__':
    data = open('input16.txt').read()
    print(part1(data, 100)[:8])
    print(part2(data, 100))
