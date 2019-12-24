#!/usr/bin/env python

import string
from collections import defaultdict, deque

import numpy as np


def name(a, b):
    return a+b if a < b else b+a

def findportals(maze):
    portals = defaultdict(list)
    h, w = maze.shape
    for y, x in np.ndindex(h-1, w-1):
        if maze[y,x] not in string.ascii_uppercase:
            continue
        if maze[y+1,x] in string.ascii_uppercase:
            c = name(maze[y,x], maze[y+1,x])
            portals[c].append((x, y-1) if maze[y-1,x] == '.' else (x, y+2))
        elif maze[y,x+1] in string.ascii_uppercase:
            c = name(maze[y,x], maze[y,x+1])
            portals[c].append((x-1, y) if maze[y,x-1] == '.' else (x+2, y))
    return portals

def load_maze(data):
    lines = data.split('\n')
    width = max(map(len, lines))
    for i, line in enumerate(lines):
        lines[i] = list(line + ' '*(width-len(line)))
    return np.array(lines)

def part1(data):
    maze = load_maze(data)
    portals = findportals(maze)
    x, y = portals['AA'][0]

    q = deque()
    seen = set()
    q.append((x, y, 0))
    while q:
        cx, cy, steps = q.popleft()
        if (cx, cy) in seen:
            continue
        seen.add((cx, cy))

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x, y = cx+dx, cy+dy
            c = maze[y,x]
            if c == '.':
                q.append((x, y, steps+1))
            elif c in string.ascii_uppercase:
                portal = name(c, maze[cy+dy*2, cx+dx*2])
                if portal == 'ZZ':
                    return steps
                elif portal == 'AA':
                    continue
                a, b = portals[portal]
                x, y = b if (cx, cy) == a else a
                q.append((x, y, steps+1))

def part2(data):
    maze = load_maze(data)
    portals = findportals(maze)
    h, w = maze.shape
    x, y = portals['AA'][0]

    q = deque()
    seen = set((x,y,0))
    q.append((x, y, 0, 0))
    while q:
        cx, cy, steps, level = q.popleft()
        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            x, y = cx+dx, cy+dy
            c = maze[y,x]
            newlevel = level
            if c in ('#', ' '):
                continue
            if c in string.ascii_uppercase:
                portal = name(c, maze[cy+dy*2, cx+dx*2])
                if portal == 'AA' or (portal == 'ZZ' and level > 0):
                    continue
                if portal == 'ZZ':
                    return steps
                a, b = portals[portal]
                outer = (x == 1 or y == 1 or x == w-2 or y == h-2)
                x, y = b if (cx, cy) == a else a
                if outer and level == 0:
                    continue
                newlevel -= (1 if outer else -1)

            if (x, y, newlevel) in seen:
                continue
            seen.add((x, y, newlevel))
            q.append((x, y, steps+1, newlevel))

if __name__ == '__main__':
    data = open('input20.txt').read()
    print(part1(data)) # 556
    print(part2(data)) # 6532
