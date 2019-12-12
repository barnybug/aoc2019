#!/usr/bin/env python

import itertools
import re
from tqdm import tqdm

import numpy as np

def parse(data):
    re_num = re.compile(r'-?\d+')
    numbers = [
        re_num.findall(line)
        for line in data.split('\n')
    ]
    pos = np.array(numbers, dtype=int)
    vel = np.zeros(pos.shape, dtype=int)
    return pos, vel

def part1(data, steps):
    pos, vel = parse(data)
    for i in range(steps):
        for j in range(len(vel)):
            vel[j] += (pos > pos[j]).sum(axis=0) - (pos < pos[j]).sum(axis=0)
        pos += vel

    pot = np.abs(pos).sum(axis=1)
    kin = np.abs(vel).sum(axis=1)
    return (pot * kin).sum()

def cycle(pos, vel):
    spos = pos.copy()
    svel = vel.copy()
    dvel = np.zeros(vel.shape, dtype=int)
    for i in tqdm(itertools.count(1)):
        gt = np.greater(pos[:,np.newaxis], pos).sum(axis=0)
        lt = np.less(pos[:,np.newaxis], pos).sum(axis=0)
        vel += gt - lt
        pos += vel
        if np.array_equal(spos, pos) and np.array_equal(svel, vel):
            return i

def part2(data):
    pos, vel = parse(data)
    cycles = [cycle(pos[:,c], vel[:,c]) for c in [0, 1, 2]]
    return np.lcm.reduce(cycles)

if __name__ == '__main__':
    data = open('input12.txt').read()
    print(part1(data, 1000))
    print(part2(data))
