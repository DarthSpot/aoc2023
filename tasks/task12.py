import regex

from tasks.abstracttask import AbstractTask

def buildvariantstring(items: [(int, (int, int))], length: int, offset: int):
    if len(items) == 0:
        return ['.' * length]
    current = items[0]
    res = []
    min = 0 if offset == 0 else 1
    for pos in range(min, current[1][1] - offset + 1):
        current_str = '.' * pos
        current_str += '#' * current[0]
        appendices = buildvariantstring(items[1::], length - len(current_str), offset + len(current_str))
        res += [current_str + x for x in appendices]

    return res


memo = {}

def buildvariantpatternstring(pattern: str, items: [(int, (int, int))], length: int, offset: int):
    key = (pattern, ','.join([str(x[0]) for x in items]), length, offset)
    if key in memo:
        return memo[key]

    if len(items) == 0:
        res = 1 if '#' not in pattern else 0
        memo[key] = res
        return res

    current = items[0]
    res = 0
    min = 0 if offset == 0 else 1
    for pos in range(min, current[1][1] - offset + 1):
        current_str = '.' * pos
        current_str += '#' * current[0]
        if matches(pattern[:len(current_str)], current_str):
            appendices = buildvariantpatternstring(pattern[len(current_str)::], items[1::], length - len(current_str), offset + len(current_str))
            res += appendices

    memo[key] = res
    return res

def matches(pattern: str, variant: str):
    if len(pattern) != len(variant):
        return False
    return all([(p == '?' or p == c) for p, c in zip(pattern, variant)])


class Task12(AbstractTask):
    def __init__(self):
        super().__init__(12)

    def simple_task(self):
        lines = self.read_file_lines()
        result = 0
        for line in [x.split() for x in lines]:
            lenghts = [int(x) for x in line[1].split(',')]
            bloblength = sum(lenghts) + len(lenghts) - 1
            map = []
            variant = len(line[0]) - bloblength
            for blob in lenghts:
                if len(map) == 0:
                    map.append((blob, (0, variant)))
                else:
                    min_pos = map[-1][1][0] + map[-1][0] + 1
                    map.append((blob, (min_pos, min_pos + variant)))
            variants = buildvariantpatternstring(line[0], map, len(line[0]), 0)
            result += variants

        return result



    def extended_task(self):
        lines = self.read_file_lines()
        result = 0
        for rawstr, rawnum in [x.split() for x in lines]:
            line = '?'.join([rawstr for _ in range(5)])
            lenghts = [int(x) for x in rawnum.split(',') * 5]
            bloblength = sum(lenghts) + len(lenghts) - 1
            map = []
            variant = len(line) - bloblength
            for blob in lenghts:
                if len(map) == 0:
                    map.append((blob, (0, variant)))
                else:
                    min_pos = map[-1][1][0] + map[-1][0] + 1
                    map.append((blob, (min_pos, min_pos + variant)))
            variants = buildvariantpatternstring(line, map, len(line), 0)
            result += variants

        return result


Task12()