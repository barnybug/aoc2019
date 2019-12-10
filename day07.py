#!/usr/bin/env python

import itertools
import numpy as np

from intcode import Code, Executor

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
