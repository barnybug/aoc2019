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

class Code:
    def __init__(self, text):
        if hasattr(text, 'read'): # file
            text = text.read()
        if isinstance(text, str):
            self.ins = list(map(int, text.split(',')))
        else:
            self.ins = text

    def __getitem__(self, i):
        return self.ins[i]

    def __setitem__(self, i, value):
        try:
            self.ins[i] = value
        except IndexError:
            self.ins.extend([0] * (i-len(self.ins)+1))
            self.ins[i] = value
    
    def copy(self):
        return Code(self.ins.copy())

    def __len__(self):
        return len(self.ins)

class Executor:
    def __init__(self, code):
        self.ins = code
        self.inputs = []
        self.runner = self.run()

    def execute(self, *inputs):
        self.inputs.extend(inputs)
        return next(self.runner)

    def complete(self, *inputs):
        self.inputs.extend(inputs)
        return list(self.runner)

    def run(self):
        def readparam(n):
            mode = (ins[ip] // (10**(n+1))) % 10
            addr = ins[ip+n]
            if mode == 1: # immediate mode
                return addr
            if mode == 2: # relative mode
                addr += relbase
            if addr >= len(ins):
                return 0
            return ins[addr]

        def writeparam(n, value):
            mode = (ins[ip] // (10**(n+1))) % 10
            addr = ins[ip+n]
            if mode == 2:
                addr += relbase
            ins[addr] = value

        ins = self.ins.copy()
        ip = 0
        relbase = 0
        output = None
        while ins[ip] != 99:
            opcode = ins[ip] % 100
            # print(f'#{ip}: {opcode}')
            if opcode in tris:
                a = readparam(1)
                b = readparam(2)
                writeparam(3, tris[opcode](a, b))
                ip += 4
            elif opcode == 3:
                # print(f'#{ip}: input {test_input} to {ins[ip+1]}')
                writeparam(1, self.inputs.pop(0))
                ip += 2
            elif opcode == 4:
                yield readparam(1)
                # print(f'{ip}#: output {output}')
                ip += 2
            elif opcode in (5, 6): # jumps
                a = readparam(1)
                b = readparam(2)
                ip = b if jumps[opcode](a) else ip+3
            elif opcode == 9: # set relbase
                relbase += readparam(1)
                ip += 2
            else:
                raise ValueError(f'Invalid instruction: {opcode}')
