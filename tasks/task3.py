import math
import re

from tasks.abstracttask import AbstractTask


class Task3(AbstractTask):
    def __init__(self):
        super().__init__(3)

    def get_field(self, map, x, y):
        width = len(map[0])
        height = len(map)
        if 0 < x < width and 0 < y < height:
            return map[y][x]
        else:
            return '.'

    def simple_task(self):
        map = self.read_file_lines()
        result = 0
        for y, row in enumerate(map):
            matches = re.finditer("\d+", row)
            for match in matches:
                span = match.span()
                num = int(row[span[0]:span[1]])
                for tx in range(span[0]-1, span[1]+1):
                    for ty in range(y-1, y+2):
                        n = self.get_field(map, tx, ty)
                        if self.issymbol(n):
                            result += int(num)

        return result

    def extended_task(self):
        map = self.read_file_lines()
        gears = {}
        for y, row in enumerate(map):
            for asterix in re.finditer("\*", row):
                span = asterix.span()
                gears[(span[0], y)] = []

        for y, row in enumerate(map):
            for match in re.finditer("\d+", row):
                span = match.span()
                num = row[span[0]:span[1]]
                neighbors = [(tx, ty) for tx in range(span[0]-1, span[1]+1) for ty in range(y-1, y+2)]
                for gear in [g for g in neighbors if self.get_field(map, g[0], g[1]) == '*']:
                    gears[gear].append(int(num))

        return sum([math.prod(x) for x in list(gears.values()) if len(x) == 2])


    def issymbol(self, n):
        if n == '.':
            return False
        elif n.isdigit():
            return False
        else:
            return True



Task3()

