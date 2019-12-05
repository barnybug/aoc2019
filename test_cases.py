import numpy as np
import pytest

import day01, day02, day03, day04, day05

def test_day01_part1():
    assert day01.part1([12]) == 2
    assert day01.part1([14]) == 2
    assert day01.part1([1969]) == 654
    assert day01.part1([100756]) == 33583

def test_day01_part2():
    assert day01.part2([12]) == 2
    assert day01.part2([1969]) == 966
    assert day01.part2([100756]) == 50346

def test_day02_part1():
    assert day02.execute([1,0,0,0,99]) == [2, 0, 0, 0, 99]
    assert day02.execute([2,3,0,3,99]) == [2, 3, 0, 6, 99]
    assert day02.execute([2,4,4,5,99,0]) == [2, 4, 4, 5, 99, 9801]
    assert day02.execute([1,1,1,4,99,5,6,0,99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]

def test_day03_part1():
    assert day03.part1(['R8,U5,L5,D3', 'U7,R6,D4,L4']) == 6
    assert day03.part1(['R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83']) == 159
    assert day03.part1(['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']) == 135

def test_day03_part2():
    assert day03.part2(['R8,U5,L5,D3', 'U7,R6,D4,L4']) == 30
    assert day03.part2(['R75,D30,R83,U83,L12,D49,R71,U7,L72', 'U62,R66,U55,R34,D71,R55,D58,R83']) == 610
    assert day03.part2(['R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51', 'U98,R91,D20,R16,D67,R40,U7,R15,U6,R7']) == 410

def test_day04_part1():
    assert day04.parts('123450-123456')[0] == 1

def test_day04_part2():
    assert day04.parts('123450-123456')[1] == 1

def test_day05_part1():
    assert day05.part1(['1002,4,3,4,33']) == None

@pytest.mark.parametrize(
    ['program', 'test_input', 'output'],
    [
        ('3,9,8,9,10,9,4,9,99,-1,8', 8, 1),
        ('3,9,8,9,10,9,4,9,99,-1,8', 0, 0),
        ('3,9,7,9,10,9,4,9,99,-1,8', 8, 0),
        ('3,9,7,9,10,9,4,9,99,-1,8', 0, 1),
        ('3,3,1108,-1,8,3,4,3,99', 8, 1),
        ('3,3,1108,-1,8,3,4,3,99', 0, 0),
        ('3,3,1107,-1,8,3,4,3,99', 8, 0),
        ('3,3,1107,-1,8,3,4,3,99', 0, 1),
        ('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', 0, 0),
        ('3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9', 9, 1),
        ('3,3,1105,-1,9,1101,0,0,12,4,12,99,1', 0, 0),
        ('3,3,1105,-1,9,1101,0,0,12,4,12,99,1', 9, 1),
        # ('', 0, 1),
        # ('', 0, 1),
    ])
def test_day05_part2(program, test_input, output):
    assert day05.part2([program], test_input) == output

@pytest.mark.parametrize(
    ['test_input', 'output'],
    [
        (7, 999),
        (8, 1000),
        (9, 1001),
    ])
def test_day05_part2_longer(test_input, output):
    program = ('3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,'
         '1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,'
         '999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99')
    assert day05.part2([program], test_input) == output

def test_day05_part2_puzzle():
    assert day05.part2(open('input05.txt'), 5) == 7731427

def test_day06_part1():
    pass

def test_day06_part2():
    pass

def test_day07_part1():
    pass

def test_day07_part2():
    pass

def test_day08_part1():
    pass

def test_day08_part2():
    pass

def test_day09_part1():
    pass

def test_day09_part2():
    pass

def test_day10_part1():
    pass

def test_day10_part2():
    pass

def test_day11_part1():
    pass

def test_day11_part2():
    pass

def test_day12_part1():
    pass

def test_day12_part2():
    pass

def test_day13_part1():
    pass

def test_day13_part2():
    pass

def test_day14_part1():
    pass

def test_day14_part2():
    pass

def test_day15_part1():
    pass

def test_day15_part2():
    pass

def test_day16_part1():
    pass

def test_day16_part2():
    pass

def test_day18_part1():
    pass

def test_day18_part2():
    pass

def test_day19_part1():
    pass

def test_day19_part2():
    pass

def test_day20_part1():
    pass

def test_day20_part2():
    pass

def test_day21_part1():
    pass

def test_day21_part2():
    pass

def test_day22_part1():
    pass

def test_day22_part2():
    pass

def test_day23_part1():
    pass

def test_day23_part2():
    pass

def test_day24_part1():
    pass

def test_day24_part2():
    pass

def test_day25_part1():
    pass

def test_day25_part2():
    pass
