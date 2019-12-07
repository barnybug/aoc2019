#!/usr/bin/env python

import itertools
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

def read1st(ins, ip):
    if (ins[ip] // 100) % 2:
        return ins[ip+1]
    return ins[ins[ip+1]]

def read2nd(ins, ip):
    if (ins[ip] // 1000) % 2:
        return ins[ip+2]
    return ins[ins[ip+2]]

class Code:
    def __init__(self, text):
        self.ins = np.genfromtxt([text], dtype=int, delimiter=',')

class Executor:
    def __init__(self, code):
        self.ins = code.ins
        self.inputs = []
        self.runner = self.run()

    def execute(self, *inputs):
        self.inputs.extend(inputs)
        return next(self.runner)

    def run(self):
        ins = self.ins.copy()
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
                # print(f'#{ip}: input {test_input} to {ins[ip+1]}')
                ins[ins[ip+1]] = self.inputs.pop(0)
                ip += 2
            elif opcode == 4:
                yield read1st(ins, ip)
                # print(f'{ip}#: output {output}')
                ip += 2
            elif opcode in (5, 6): # jumps
                a = read1st(ins, ip)
                b = read2nd(ins, ip)
                ip = b if jumps[opcode](a) else ip+3
            else:
                raise ValueError(f'Invalid instruction: {opcode}')

def chain(code, phases):
    output = 0
    for phase in phases:
        prog = Executor(code)
        output = prog.execute(phase, output)
    return output

def part1(text):
    code = Code(text)
    max_signal = max(
        chain(code, phases)
        for phases in itertools.permutations(range(5)))
    return max_signal

def feedback(code, phases):
    output = 0
    amps = [
        Executor(code)
        for phase in phases
    ]
    for amp, phase in zip(amps, phases):
        amp.inputs.append(phase)
    while True:
        for amp in amps:
            # amp.inputs.append(output)
            try:
                output = amp.execute(output)
            except StopIteration:
                return output
    return output

def part2(text):
    code = Code(text)
    max_signal = max(
        feedback(code, phases)
        for phases in itertools.permutations(range(5, 10)))
    return max_signal

if __name__ == '__main__':
    print(part1(open('input07.txt').read()))
    print(part2(open('input07.txt').read()))
