import math
import re

from tasks.abstracttask import AbstractTask

def finddistancebetween(start, finish, instructions, data):
    length = len(instructions)
    nodes = {x.group(1): (x.group(2), x.group(3)) for x in
             [re.match("([A-Z0-9]+) = \(([A-Z0-9]+), ([A-Z0-9]+)\)", x) for x in data]}
    reversedMap = {}
    for node in nodes:
        left = [k for k, v in nodes.items() if v[0] == node]
        right = [k for k, v in nodes.items() if v[1] == node]
        reversedMap[node] = (left, right)
    endconditions = set([(x,0) for x in start])
    current = []
    for i in range(len(instructions)):
        current.append((finish, i))
    cache = set()
    steps = 0
    while not len(endconditions.intersection(current)) > 0:
        steps += 1
        steplist = []
        for elem in current:
            if elem not in cache:
                cache.add(elem)
                pos = (length + elem[1] - 1) % length
                ins = instructions[pos]
                steplist += [(x, pos) for x in reversedMap[elem[0]][1 if ins == 'R' else 0]]
        current = steplist

    return steps

class Task8(AbstractTask):
    def __init__(self):
        super().__init__(8)

    def simple_task(self):
        lines = self.read_file_lines()
        return finddistancebetween(['AAA'], 'ZZZ', lines[0], lines[2:])

    def extended_task(self):
        lines = self.read_file_lines()
        nodes = [x.split()[0] for x in lines[2:]]
        starts = [k for k in nodes if k.endswith('A')]
        ends = {k:[] for k in nodes if k.endswith('Z')}

        for k,v in ends.items():
            distance = finddistancebetween(starts, k, lines[0], lines[2:])
            if distance > 0:
                v.append(distance)

        results = [min(v) for k,v in ends.items()]
        return math.lcm(*results)


Task8()