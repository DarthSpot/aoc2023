import re
from functools import reduce

from tasks.abstracttask import AbstractTask

def hash(input: str):
    return reduce(lambda x, y: ((x + y) * 17) % 256, [ord(c) for c in input], 0)

class Task15(AbstractTask):
    def __init__(self):
        super().__init__(15)

    def simple_task(self):
        input = self.read_file_string().strip().split(",")
        return sum([hash(v) for v in input])


    def extended_task(self):
        input = self.read_file_string().split(",")
        inputs = [(match.group(1,2,3)) for match in [re.match(r"([a-z]+)([=-])(\d?)", v) for v in input]]
        box = {x:[] for x in [x for x in range(0,256)]}
        boxh = {}
        for v in inputs:
            h = hash(v[0])
            if v[1] == '-':
                if v[0] in box[h]:
                    box[h].remove(v[0])
            elif v[1] == '=':
                if v[0] not in box[h]:
                    box[h].append(v[0])
                boxh[v[0]] = int(v[2])

        res = [[(1 + k) * (1 + idx) * boxh[l] for idx, l in enumerate(v)] for k,v in box.items()]
        return sum([sum(v) for v in res])


Task15()