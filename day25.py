#!/usr/bin/env python

from dataclasses import dataclass
import itertools
from collections import defaultdict
import re

import numpy as np

from intcode import Code, Executor

re_dirs = re.compile(r'Doors here lead:\n- (.+?)\n\n', re.M | re.S)
re_items = re.compile(r'Items here:\n- (.+?)\n\n', re.M | re.S)

dirs = {
    'north': (0, -1),
    'south': (0, 1),
    'east': (1, 0),
    'west': (-1, 0),
}
opposite = {
    'north': 'south',
    'south': 'north',
    'east': 'west',
    'west': 'east',
}
item_blacklist = set([
    'escape pod',
    'giant electromagnet',
    'infinite loop',
    'molten lava',
    'photons',
])

@dataclass
class Room:
    doors: list
    items: list

    @classmethod
    def parse(cls, text):
        m = re_dirs.search(text)
        doors = m.group(1).split('\n- ')

        if m := re_items.search(text):
            items = m.group(1).split('\n- ')
        else:
            items = []
        
        return Room(doors, items)

class Game:
    def __init__(self, data):
        self.exe = Executor(Code(data))

    def send(self, command):
        print(command, end='')
        self.exe.inputs.extend(ord(c) for c in command+'\n')

    def receive(self):
        text = ''.join(map(chr, itertools.takewhile(bool, self.exe.runner)))
        print(text, end='')
        return text

    def step(self, door):
        self.send(door)
        return Room.parse(self.receive())

    def take(self, item):
        self.send(f'take {item}')
        self.receive()

    def drop(self, item):
        self.send(f'drop {item}')
        self.receive()

    def interactive(self):
        while True:
            self.send(input())
            self.receive()

def part1(data):
    game = Game(data)

    commands = [
        # Start
        'north',
        'west',
        'west',
        'east',
        'east',
        'south',
        # Start ([N]EW)
        'west',
        # Stranded (N[E]S)
        'north',
        'south',
        'east', # Start [N]E[W]
        'east', # Science Lab N[EW] (E leads nowhere)
        'north', # Observatory [ES]W (E leads to trap)
        'west', # Crew Quarters N[E]W
        'north', # Storage
        'south', # Crew Quarter [NE]W
        'west', # Gift Wrapping Center
        'south', # Kitchen [N]W
        'west', # Hot Chocolate Fountain E
        'east',
        'north', # Gif Wrapping Center
        'north', # Engineering
        'west', # Security Checkpoint
    ]

    game.receive() # Start

    items = []
    for command in commands:
        room = game.step(command)
        for item in room.items:
            if item in item_blacklist:
                continue
            items.append(item)
            game.take(item)

    current = set(items)
    for n in range(1, len(items)+1):
        for comb in itertools.combinations(items, n):
            target = set(comb)
            drop = current - target
            take = target - current
            for d in drop:
                game.drop(d)
            for t in take:
                game.take(t)
            current = target

            game.send('south')
            text = game.receive()
            if 'ejected' not in text:
                print('items:', current)
                m = re.search(r'\d+', text)
                return m.group(0)

if __name__ == '__main__':
    data = open('input25.txt').read()
    print(part1(data))
