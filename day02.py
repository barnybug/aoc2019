#!/usr/bin/env python

import numpy as np

def execute(ins):
    ins = np.array(ins)
    ip = 0
    while ins[ip] != 99:
        o = ins[ip]
        if o not in (1, 2):
            raise ValueError(f'Invalid instruction: {ins[ip]}')
        op = np.sum if o == 1 else np.prod
        ins[ins[ip+3]] = op(ins[ins[ip+1:ip+3]])
        ip += 4
    return ins.tolist()

def part1(lines):
    ins = np.genfromtxt(lines, dtype=int, delimiter=',')
    ins[1] = 12
    ins[2] = 2
    result = execute(ins)
    return result[0]

def part2(lines):
    original = np.genfromtxt(lines, dtype=int, delimiter=',')
    for noun in range(0, 99):
        for verb in range(0, 99):
            ins = original.copy()
            ins[1] = noun
            ins[2] = verb
            result = execute(ins)
            if result[0] == 19690720:
                return noun*100+verb
    return None

if __name__ == '__main__':
    print(part1(open('input02.txt')))
    print(part2(open('input02.txt')))
