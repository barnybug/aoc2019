import numpy as np
from dataclasses import dataclass
import pytest

import day01, day02, day03, day04, day05, day06, day07, day08, day09
import day10, day11, day12, day13, day14, day15, day16, day17
from intcode import Executor, Code

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
    assert day06.part1('''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L'''.split()) == 42
    assert day06.part1(open('input06.txt')) == 171213

def test_day06_part2():
    assert day06.part2('''COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L
K)YOU
I)SAN'''.split()) == 4

def test_day07_part1():
    day07.part1('3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0') == 43210
    day07.part1('3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0') == 54321
    day07.part1('3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0') == 65210

def test_day07_part2():
    day07.part2('3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5') == 139629729
    day07.part2('3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10') == 18216

def test_day08_part1():
    assert day08.part1('123456789012', (3, 2)) == 1

def test_day08_part2():
    assert day08.part2('0222112222120000', (2, 2)) == ' #\n# '

def test_intcode():
    assert Executor(Code('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99')).complete() == [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    assert Executor(Code('1102,34915192,34915192,7,4,7,99,0')).complete() == [1219070632396864]
    assert Executor(Code('104,1125899906842624,99')).complete() == [1125899906842624]

def test_day09_part1():
    code = Code(open('input09.txt'))
    assert day09.part1(code) == [3340912345]

def test_day09_part2():
    code = Code(open('input09.txt'))
    assert day09.part2(code) == [51754]

def test_day10_part1():
    assert day10.part1('''.#..#
.....
#####
....#
...##''') == ((3, 4), 8)
    assert day10.part1('''......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####''') == ((5, 8), 33)
    assert day10.part1('''#.#...#.#.
.###....#.
.#....#...
##.#.#.#.#
....#.#.#.
.##..###.#
..#...##..
..##....##
......#...
.####.###.''') == ((1, 2), 35)
    assert day10.part1('''.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..''') == ((6, 3), 41)
    assert day10.part1('''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##''') == ((11, 13), 210)

def test_day10_part2():
    assert day10.part2('''.#....#####...#..
##...##.#####..##
##...#...#.#####.
..#.....X...###..
..#.#.....#....##''', None, 35) == 1403

    assert day10.part2('''.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##''', (11, 13)) == 802

class DummyExecutor:
    pass

def test_day11_part1():
    exe = DummyExecutor()
    exe.runner = iter([1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0])
    assert len(day11.robot(exe)) == 6

def test_day11_part2():
    pass

def test_day12_part1():
    assert day12.part1('''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>''', 10) == 179
    assert day12.part1('''<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>''', 100) == 1940

def test_day12_part2():
    assert day12.part2('''<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>''') == 2772
    assert day12.part2('''<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>''') == 4686774924

def test_day13_part1():
    pass

def test_day13_part2():
    pass

day14_1 = '''10 ORE => 10 A
1 ORE => 1 B
7 A, 1 B => 1 C
7 A, 1 C => 1 D
7 A, 1 D => 1 E
7 A, 1 E => 1 FUEL'''

day14_2 = '''9 ORE => 2 A
8 ORE => 3 B
7 ORE => 5 C
3 A, 4 B => 1 AB
5 B, 7 C => 1 BC
4 C, 1 A => 1 CA
2 AB, 3 BC, 4 CA => 1 FUEL'''

day14_3 = '''157 ORE => 5 NZVS
165 ORE => 6 DCFZ
44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL
12 HKGWZ, 1 GPVTF, 8 PSHF => 9 QDVJ
179 ORE => 7 PSHF
177 ORE => 5 HKGWZ
7 DCFZ, 7 PSHF => 2 XJWVT
165 ORE => 2 GPVTF
3 DCFZ, 7 NZVS, 5 HKGWZ, 10 PSHF => 8 KHKGT'''

day14_4 = '''2 VPVL, 7 FWMGM, 2 CXFTF, 11 MNCFX => 1 STKFG
17 NVRVD, 3 JNWZP => 8 VPVL
53 STKFG, 6 MNCFX, 46 VJHF, 81 HVMC, 68 CXFTF, 25 GNMV => 1 FUEL
22 VJHF, 37 MNCFX => 5 FWMGM
139 ORE => 4 NVRVD
144 ORE => 7 JNWZP
5 MNCFX, 7 RFSQX, 2 FWMGM, 2 VPVL, 19 CXFTF => 3 HVMC
5 VJHF, 7 MNCFX, 9 VPVL, 37 CXFTF => 6 GNMV
145 ORE => 6 MNCFX
1 NVRVD => 8 CXFTF
1 VJHF, 6 MNCFX => 4 RFSQX
176 ORE => 6 VJHF'''

day14_5 = '''171 ORE => 8 CNZTR
7 ZLQW, 3 BMBT, 9 XCVML, 26 XMNCP, 1 WPTQ, 2 MZWV, 1 RJRHP => 4 PLWSL
114 ORE => 4 BHXH
14 VRPVC => 6 BMBT
6 BHXH, 18 KTJDG, 12 WPTQ, 7 PLWSL, 31 FHTLT, 37 ZDVW => 1 FUEL
6 WPTQ, 2 BMBT, 8 ZLQW, 18 KTJDG, 1 XMNCP, 6 MZWV, 1 RJRHP => 6 FHTLT
15 XDBXC, 2 LTCX, 1 VRPVC => 6 ZLQW
13 WPTQ, 10 LTCX, 3 RJRHP, 14 XMNCP, 2 MZWV, 1 ZLQW => 1 ZDVW
5 BMBT => 4 WPTQ
189 ORE => 9 KTJDG
1 MZWV, 17 XDBXC, 3 XCVML => 2 XMNCP
12 VRPVC, 27 CNZTR => 2 XDBXC
15 KTJDG, 12 BHXH => 5 XCVML
3 BHXH, 2 VRPVC => 7 MZWV
121 ORE => 7 VRPVC
7 XCVML => 6 RJRHP
5 BHXH, 4 VRPVC => 5 LTCX'''

def test_day14_part1():
    assert day14.part1(day14_1) == 31
    assert day14.part1(day14_2) == 165
    assert day14.part1(day14_3) == 13312
    assert day14.part1(day14_4) == 180697
    assert day14.part1(day14_5) == 2210736

def test_day14_part2():
    assert day14.part2(day14_3) == 82892753
    assert day14.part2(day14_4) == 5586022
    assert day14.part2(day14_5) == 460664

def test_day15_part1():
    pass

def test_day15_part2():
    pass

def test_day16_part1():
    assert day16.part1('12345678', 1) == '48226158'
    assert day16.part1('12345678', 2) == '34040438'
    assert day16.part1('12345678', 3) == '03415518'
    assert day16.part1('12345678', 4) == '01029498'

    assert day16.part1('80871224585914546619083218645595', 100)[:8] == '24176176'
    assert day16.part1('19617804207202209144916044189917', 100)[:8] == '73745418'
    assert day16.part1('69317163492948606335995924319873', 100)[:8] == '52432133'

def test_day16_part2():
    assert day16.part2('03036732577212944063491565474664', 100) == '84462026'
    assert day16.part2('02935109699940807407585447034323', 100) == '78725270'
    assert day16.part2('03081770884921959731165446850517', 100) == '53553731'

def test_day17_part1_map():
    s = '''..#..........
..#..........
#######...###
#.#...#...#.#
#############
..#...#...#..
..#####...^..'''
    assert day17.part1_map(s) == 76

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
