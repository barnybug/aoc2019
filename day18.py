#!/usr/bin/env python

from collections import deque
import string
import numpy as np

def connections(grid, x, y):
    # get the connections of x, y
    seen = set()
    # breadth first search
    q = deque()
    seen.add((x, y))
    q.append((x, y, 0, set()))
    while q:
        x, y, steps, doors = q.popleft()
        # where can we go from x, y?
        for p in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            c = grid[p[1], p[0]]
            if c == '#':
                continue 
            if p in seen:
                continue
            seen.add(p)
            if c in string.ascii_uppercase:
                q.append((p[0], p[1], steps+1, doors | set(c.lower())))
                continue
            
            q.append((p[0], p[1], steps+1, doors))
            if c in string.ascii_lowercase:
                yield c, steps+1, doors

def network(grid):
    # build a graph of the connections between keys
    letters = np.argwhere(np.isin(grid, list(string.ascii_lowercase) + list('@1234')))
    net = {}
    for y, x in letters:
        letter = grid[y, x]
        conns = connections(grid, x, y)
        net[letter] = list(conns)
    nkeys = np.isin(grid, list(string.ascii_lowercase)).sum()
    return net, nkeys

def routes(net, at, nkeys):
    q = deque()
    quickest = {(at, frozenset()): 0}
    q.append((at, frozenset()))
    while q:
        at, keys = q.popleft()
        total = quickest[(at, keys)]
        for to, steps, doors in net[at]:
            if to in keys:
                continue
            if not doors.issubset(keys):
                continue
            keys_now = keys | set(to)
            # The cunning part - if we've found a quicker route to the same result
            # (at the same node with the same keys), then we just need to update the
            # quickest dict. If it's a worse route, just discard. Otherwise,
            # record in quickest and add to queue.
            try:
                previous = quickest[(to, keys_now)]
                quickest[(to, keys_now)] = min(total+steps, previous)
            except KeyError:
                quickest[(to, keys_now)] = total+steps
                q.append((to, keys_now))
            if len(keys_now) == nkeys:
                yield total+steps

def part1(data):
    grid = np.array([list(line) for line in data.split()])
    net, nkeys = network(grid)
    answers = routes(net, '@', nkeys)
    return min(answers)

def routes4(net, robots, nkeys):
    q = deque()
    quickest = {(robots, frozenset()): 0}
    q.append((robots, frozenset()))
    while q:
        robots, keys = q.popleft()
        total = quickest[(robots, keys)]
        for i in range(4):
            at = robots[i]
            for to, steps, doors in net[at]:
                if to in keys:
                    continue
                if not doors.issubset(keys):
                    continue
                keys_now = keys | set(to)
                # The cunning part - if we've found a quicker route to the same result
                # (at the same node with the same keys), then we just need to update the
                # quickest dict. If it's a worse route, just discard. Otherwise,
                # record in quickest and add to queue.
                tos = robots[:i] + (to,) + robots[i+1:]
                state = (tos, keys_now)
                try:
                    previous = quickest[state]
                    quickest[state] = min(total+steps, previous)
                except KeyError:
                    quickest[state] = total+steps
                    q.append(state)
                if len(keys_now) == nkeys:
                    yield total+steps

def part2(data):
    grid = np.array([list(line) for line in data.split('\n')])
    # modify grid into 4 vaults
    oy, ox = np.argwhere(grid == '@')[0]
    grid[oy-1:oy+2,ox-1:ox+2] = [['1', '#', '2'], ['#', '#', '#'], ['4', '#', '3']]
    net, nkeys = network(grid)
    answers = routes4(net, ('1','2','3','4'), nkeys)
    return min(answers)

if __name__ == '__main__':
    data = open('input18.txt').read()
    print(part1(data))
    print(part2(data))
