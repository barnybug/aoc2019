#!/usr/bin/env python

import itertools
from collections import defaultdict
import numpy as np

def warshall1(A):
    # Warshall's algorithm (simple reachable version)
    T = A.copy()
    for j in range(len(A)):
        for i in range(len(A)):
            if T[i][j]:
                T[i] = T[i] | T[j]
    return T

def warshall(A):
    # Warshall's algorithm (minimum distance version)
    T = A.copy()
    for k in range(len(A)):
        T = np.minimum(T, T[np.newaxis,k,:] + T[:,k,np.newaxis]) 
    return T

def loadmatrix(lines, zero, one):
    pairs = [line.strip().split(')') for line in lines]
    labels = sorted(set(label for pair in pairs for label in pair))
    indices = {label: i for i, label in enumerate(labels)}
    size = len(labels)
    # create an adjacency matrix
    A = np.full((size, size), zero)
    for a, b in pairs:
        A[indices[b], indices[a]] = one
    return A, pairs, indices

def part1(lines):
    A, _, _ = loadmatrix(lines, False, True)
    T = warshall1(A)
    return T.sum()

def part2(lines):
    A, pairs, indices = loadmatrix(lines, np.inf, 1)
    A = np.minimum(A, A.T) # make bidirectional
    lookup = {b: a for a, b in pairs}
    you = indices[lookup['YOU']]
    san = indices[lookup['SAN']]
    T = warshall(A)
    return T[you,san]

if __name__ == '__main__':
    # print(part1(open('input06.txt')))
    print(part2(open('input06.txt')))
