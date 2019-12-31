#!/usr/bin/env python

import numpy as np
from intcode import Code, Executor

def part1(data):
    code = Code(data)
    computers = [
        Executor(code, [i, -1])
        for i in range(50)
    ]
    while True:
        for i, computer in enumerate(computers):
            addr, x, y = computer.executen(3)
            if addr == 255:
                return y
            if addr is not None:
                computers[addr].inputs.extend([x, y])

    return None

def part2(data):
    code = Code(data)
    computers = [
        Executor(code, [i, -1])
        for i in range(50)
    ]
    nat = []
    ys = set()
    while True:
        blocked = 0
        for i, computer in enumerate(computers):
            addr, x, y = computer.executen(3)
            if addr is None:
                blocked += 1
                continue
            if addr == 255:
                nat = [x, y]
            else:
                computers[addr].inputs.extend([x, y])

        if blocked == 50:
            if nat[1] in ys:
                return nat[1]
            ys.add(nat[1])
            computers[0].inputs.extend(nat)

if __name__ == '__main__':
    data = open('input23.txt').read()
    # print(part1(data))
    print(part2(data))
