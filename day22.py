#!/usr/bin/env python

from dataclasses import dataclass
import re

re_deal_inc = re.compile(r'deal with increment (\d+)')
re_reverse = re.compile(r'deal into new stack')
re_cut = re.compile(r'cut (-?\d+)')

def deal(steps, m, i):
    for step in steps:
        if match := re_deal_inc.match(step):
            n = int(match.group(1))
            # (n * i) mod m = c
            i = (i * n) % m
        elif match := re_reverse.match(step):
            i = m - i - 1
        elif match := re_cut.match(step):
            n = int(match.group(1))
            i = (i - n) % m
        else:
            raise ValueError(f'Failed to parse: {step}')

    return i

@dataclass
class Linear(object):
    # c = a + bx mod m
    a: int
    b: int
    m: int

    def __call__(self, l):
        assert self.m == l.m
        # f(x) = a1 + b1*x to g(x) = a2 + b2*x
        # apply f(g(x)):
        # f = a1 + b1*a2 + b1*b2*x
        a = (self.a + self.b*l.a) % self.m
        b = (self.b*l.b) % self.m
        return Linear(a, b, self.m)

    def evaluate(self, x):
        return (self.a + self.b * x) % self.m

def revsteps(steps, m):
    l = Linear(0, 1, m) # c = 0 + 1x (identity)
    for step in reversed(steps):
        if match := re_deal_inc.match(step):
            n = int(match.group(1))
            # Forward: (n * i) mod m = c
            # Backward: i = c * n^-1 mod m
            # i = pow(n, -1, m) * i
            l = Linear(0, pow(n, -1, m), m)(l)
        elif match := re_reverse.match(step):
            # i = m - i - 1
            # i = (m - 1 - i) = -1 - i
            l = Linear(-1, -1, m)(l)
        elif match := re_cut.match(step):
            # i = (n + i) % m
            a = int(match.group(1))
            l = Linear(a, 1, m)(l)
        else:
            raise ValueError(f'Failed to parse: {step}')
    return l

def dealrev(steps, m, i):
    l = revsteps(steps, m)
    i = l.evaluate(i)
    return i

def dealrevtimes(steps, m, i, n):
    l = revsteps(steps, m)
    f = Linear(0, 1, m)
    # l applied n times
    # Break n times down into binary components, and calculate
    # the 'sum' of the applications
    while n:
        if n % 2:
            # apply for this digit
            f = l(f)
        n //= 2
        l = l(l) # double application (next binary digit)
    i = f.evaluate(i)
    return i

def part1(data):
    return deal(data, 10007, 2019)

def part2(data):
    return dealrevtimes(data, m=119315717514047, i=2020, n=101741582076661)

if __name__ == '__main__':
    data = open('input22.txt').readlines()
    print(part1(data))
    print(part2(data))
