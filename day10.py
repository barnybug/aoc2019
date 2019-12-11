#!/usr/bin/env python

import itertools
import numpy as np

def calc1(data):
    a = np.array([list(line) for line in data.split()])
    coords = np.argwhere(a.T == '#')
    # print('coords', coords)

    counts = np.zeros(coords.shape[0], int)
    for i in range(len(coords)):
        cx, cy = coords[i]
        rest = np.delete(coords, i, axis=0)
        rest -= coords[i]
        # print('considering:', cx, cy)
        # print('rebased', rest)
        rest = np.array(sorted(rest, key=lambda p: np.max(np.abs(p))))
        # print('sorted', rest)
        masked = np.zeros(len(rest), bool)
        for j in range(len(rest)-1):
            if masked[j]:
                continue
            # print('masking:', rest[j])
            x, y = rest[j] // np.gcd(*rest[j])
            # eg (4, 2) masks (2, 1), (4, 2), (6, 3)
            # multiples
            ds = rest[j+1:,0] * y == rest[j+1:,1] * x
            # print(ds)
            # same quarter
            q = ((rest[j+1:] * rest[j]) >= 0).all(axis=1)
            # print(q)
            masked[j+1:] = masked[j+1:] | (ds & q)
            # print('result:', masked)

        # print('amsked:', masked)
        sees = (~masked).sum()
        counts[i] = sees

    return coords, counts

def test1(data):
    _, counts = calc1(data)
    return tuple(coords[np.argmax(counts)])

def quarter(q, ratio, vapourized, survivors):
    # group by matching ratio, sorted by first in sweep
    for _, group in itertools.groupby(sorted(q, key=ratio), key=ratio):
        # sort by distance
        order = sorted(group, key=lambda p: abs(p[0])+abs(p[1]))
        vapourized.append(order[0])
        survivors.extend(order[1:])

def part1(data):
    coords, counts = calc1(data)
    pos = coords[np.argmax(counts)]
    return tuple(pos), max(counts)

def part2(data, base=None, number=199):
    a = np.array([list(line) for line in data.split()])
    if base:
        a[base[1],base[0]] = 'X'
    coords = np.argwhere(a.T == '#')
    base = np.argwhere(a.T == 'X')
    coords -= base
    vapourized = []

    while len(coords):
        q1 = coords[(coords[:,0] >= 0) & (coords[:,1] < 0)]
        q2 = coords[(coords[:,0] > 0) & (coords[:,1] >= 0)]
        q3 = coords[(coords[:,0] <= 0) & (coords[:,1] > 0)]
        q4 = coords[(coords[:,0] < 0) & (coords[:,1] <= 0)]

        survivors = []
        quarter(q1, lambda p: abs(p[0]/p[1]), vapourized, survivors)
        quarter(q2, lambda p: abs(p[1]/p[0]), vapourized, survivors)
        quarter(q3, lambda p: abs(p[0]/p[1]), vapourized, survivors)
        quarter(q4, lambda p: abs(p[1]/p[0]), vapourized, survivors)

        coords = np.array(survivors)

    vapourized = np.array(vapourized) + base
    x, y = vapourized[number]
    return x*100+y

if __name__ == '__main__':
    data = open('input10.txt').read()
    pos, count = part1(data)
    print(count)
    print(part2(data, pos))
