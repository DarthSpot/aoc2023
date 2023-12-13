from tasks.abstracttask import AbstractTask

def getmirror(map, extended):
    mapdata = []
    for row in map:
        current = {}
        for idx in range(1, len(row)):
            left = row[0:idx][::-1]
            right = row[idx:]
            z = list(zip(left, right))
            current[idx] = len([x for x in [a == b for a, b in z] if not x])
        mapdata.append(current)
    errors = [(idx, [y[idx] for y in mapdata]) for idx in range(1, len(map[0]))]
    result = [idx for idx, x in errors if sum(x) == (1 if extended else 0)]
    if len(result) == 1:
        return result[0]
    return None

class Task13(AbstractTask):
    def __init__(self):
        super().__init__(13)

    def simple_task(self):
        lines = self.read_file_string()
        input = [data.strip().split("\n") for data in lines.split("\n\n")]

        result = 0
        for map in input:
            turnedmap = [[map[y][x] for y in range(len(map))] for x in range(len(map[0]))]
            h = getmirror(map, False)
            v = getmirror(turnedmap, False)
            if h is not None:
                result += h
            if v is not None:
                result += 100 * v

        return result



    def extended_task(self):
        lines = self.read_file_string()
        input = [data.strip().split("\n") for data in lines.split("\n\n")]

        result = 0
        for map in input:
            turnedmap = [[map[y][x] for y in range(len(map))] for x in range(len(map[0]))]
            h = getmirror(map, True)
            v = getmirror(turnedmap, True)
            if h is not None:
                result += h
            if v is not None:
                result += 100 * v
        return result



Task13()