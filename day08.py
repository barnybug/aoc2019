#!/usr/bin/env python

import numpy as np

def decode(data, size):
    image = np.array([int(c) for c in data], dtype=int)
    return image.reshape((-1, size[1], size[0]))

def part1(data, size):
    image = decode(data, size)
    zeros = (image == 0).sum(axis=(1,2))
    min_zeros = np.argmin(zeros)
    layer = image[min_zeros]
    return (layer == 1).sum() * (layer == 2).sum()

def part2(data, size):
    image = decode(data, size)
    result = image[-1]
    for layer in reversed(image[:-1]):
        result = result * (layer == 2) + layer * (layer != 2)

    result = np.where(result == 1, '#', ' ')
    return '\n'.join(''.join(row) for row in result)

if __name__ == '__main__':
    data = open('input08.txt').read()
    size = (25, 6)
    print(part1(data, size), '\n')
    print(part2(data, size))
