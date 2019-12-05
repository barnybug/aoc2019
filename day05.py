#!/usr/bin/env python

import operator
import numpy as np

tris = {
    1: operator.add,
    2: operator.mul,
    7: lambda a, b: int(a < b),
    8: lambda a, b: int(a == b),
}

jumps = {
    5: lambda a: a != 0,
    6: lambda a: a == 0,
}

operands = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
}

def read1st(ins, ip):
    if (ins[ip] // 100) % 2:
        return ins[ip+1]
    return ins[ins[ip+1]]

def read2nd(ins, ip):
    if (ins[ip] // 1000) % 2:
        return ins[ip+2]
    return ins[ins[ip+2]]

def execute(ins, test_input):
    ins = np.array(ins)
    ip = 0
    output = None
    while ins[ip] != 99:
        opcode = ins[ip] % 100
        # print(f'#{ip}: {opcode}')
        if opcode in tris:
            a = read1st(ins, ip)
            b = read2nd(ins, ip)
            c = ins[ip+3]
            ins[c] = tris[opcode](a, b)
            ip += 4
        elif opcode == 3:
            print(f'#{ip}: input {test_input} to {ins[ip+1]}')
            ins[ins[ip+1]] = test_input
            ip += 2
        elif opcode == 4:
            output = read1st(ins, ip)
            print(f'{ip}#: output {output}')
            ip += 2
        elif opcode in (5, 6): # jumps
            a = read1st(ins, ip)
            b = read2nd(ins, ip)
            ip = b if jumps[opcode](a) else ip+3
        else:
            raise ValueError(f'Invalid instruction: {opcode}')
    return output

def part1(lines):
    ins = np.genfromtxt(lines, dtype=int, delimiter=',')
    result = execute(ins, 1)
    return result

def part2(lines, i):
    ins = np.genfromtxt(lines, dtype=int, delimiter=',')
    return execute(ins, i)

if __name__ == '__main__':
    print(part1(open('input05.txt')))
    print(part2(open('input05.txt'), 5))
