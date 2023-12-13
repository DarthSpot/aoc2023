from tasks.abstracttask import AbstractTask


def getmirror(map):
    mirror = set(range(len(map[0])))
    for row in map:
        current = []
        for idx in range(1, len(row)):
            left = row[0:idx][::-1]
            right = row[idx:]
            z = list(zip(left, right))
            if all([a == b for a,b in z]):
                current.append(idx)
        mirror = mirror.intersection(current)
        if len(mirror) == 0:
            return None
    return list(mirror)[0]

def getsmudgedline(map, oldmirror):
    mapdata = []
    for row in map:
        current = {}
        for idx in range(1, len(row)):
            if oldmirror is not None or oldmirror != idx:
                left = row[0:idx][::-1]
                right = row[idx:]
                z = list(zip(left, right))
                current[idx] = len([x for x in [a == b for a,b in z] if not x])
        mapdata.append(current)
    errors = [(idx, [y[idx] for y in mapdata]) for idx in range(1, len(map[0]))]
    singularerrors = [idx for idx, x in errors if sum(x) == 1]
    if len(singularerrors) == 1:
        return singularerrors[0]
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
            h = getmirror(map)
            v = getmirror(turnedmap)
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
            h = getmirror(map)
            v = getmirror(turnedmap)
            hx = getsmudgedline(map, h)
            vx = getsmudgedline(turnedmap, v)
            if hx is not None:
                result += hx
            if vx is not None:
                result += 100 * vx
        return result



Task13()