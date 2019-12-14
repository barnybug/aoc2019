#!/usr/bin/env python

from collections import Counter
import math
import numpy as np

def parse_part(part):
    n, name = part.split(' ')
    return name, int(n)

def parse_line(line):
    left, right = line.split(' => ')
    parts = [parse_part(part) for part in left.split(', ')]
    return parts, parse_part(right)

def parse(data):
    rules = [parse_line(line) for line in data.split('\n')]
    return {rule[1][0]: rule for rule in rules}

def solve(lrules, fuel):
    req = Counter({'FUEL': fuel})
    while True:
        try:
            item = next(item for item in req if item != 'ORE' and req[item] > 0)
        except StopIteration:
            break
        left, right = lrules[item]
        times = math.ceil(req[item] / right[1])
        req[item] -= right[1] * times
        if req[item] == 0:
            del req[item]
        for name, i in left:
            req[name] += i * times
    return req['ORE']

def part1(data):
    lrules = parse(data)
    return solve(lrules, 1)

def part2(data):
    lrules = parse(data)
    target = 1e12
    lower = int(target / solve(lrules, 1))
    upper = lower * 10
    while True:
        mid = int((upper + lower)/2)
        ore = solve(lrules, mid)
        if mid == lower:
            return mid
        if ore > target:
            upper = mid
        elif ore < target:
            lower = mid

if __name__ == '__main__':
    data = open('input14.txt').read()
    print(part1(data))
    print(part2(data))
