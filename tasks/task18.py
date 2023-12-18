from tasks.abstracttask import AbstractTask

def addtuple(a, b):
    return tuple(map(sum, zip(a, b)))

def calcarea(data: [(str, int)]):

    dirs = {'U': (0, -1),
            'R': (1, 0),
            'L': (-1, 0),
            'D': (0, 1)}

    points = [(0, 0)]
    perimeter = 0
    for dir, dist in data:
        movx, movy = dirs[dir]
        mov = (movx * dist, movy * dist)
        pos = points[-1]
        new_pos = addtuple(pos, mov)
        points.append(new_pos)
        perimeter += dist

    return int(area(points) + perimeter / 2 + 1)

def area(points):
    result = 0

    pairs = list(zip(points, points[1:] + [points[0]]))

    for a,b in pairs:
        x1, x2 = a
        y1, y2 = b
        result += x1 * y2 - x2 * y1

    return abs(result) / 2

class Task18(AbstractTask):
    def __init__(self):
        super().__init__(18)
    
    def simple_task(self):
        lines = [line.split() for line in self.read_file_lines()]
        return calcarea([(x, int(y)) for x,y,z in lines])

    
    def extended_task(self):
        lines = [line.split() for line in self.read_file_lines()]
        dirs = {
            '0': 'R',
            '1': 'D',
            '2': 'L',
            '3': 'U'
        }
        data = [(dirs[s[-2]], int(s[2:7], 16)) for _, _, s in lines]
        return calcarea(data)


Task18()
