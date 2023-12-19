from tasks.abstracttask import AbstractTask

def get_points_of_edge(start: (int, int), end: (int, int)):
    result = []
    for y in range(min(start[1], end[1]), max(start[1], end[1]) + 1):
        for x in range(min(start[0], end[0]), max(start[0], end[0]) + 1):
            if (x, y) != start:
                result.append((x,y))
    return result


def add_tuple(a, b):
    return tuple(map(sum, zip(a, b)))


class Task16(AbstractTask):
    def __init__(self):
        super().__init__(16)
    
    def simple_task(self):
        lines = self.read_file_lines()
        lines = """.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....""".split("\n")
        data = {}

        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c != '.':
                    data[(x, y)] = c

        maxx = len(lines[0]) - 1
        maxy = len(lines) - 1

        dirchanges = {
            ('/', 0): [3],
            ('/', 3): [0],
            ('/', 2): [1],
            ('/', 1): [2],
            ('\\', 0): [1],
            ('\\', 1): [0],
            ('\\', 2): [3],
            ('\\', 3): [2],
            ('|', 0): [1, 3],
            ('|', 1): [1],
            ('|', 2): [1, 3],
            ('|', 3): [3],
            ('-', 0): [0],
            ('-', 1): [0, 2],
            ('-', 2): [2],
            ('-', 3): [0, 2],
        }

        ends = [((-1, 0), 0)]
        energized = set()
        while len(ends) > 0:
            (endx, endy), endd = ends.pop(0)
            xs = [((kx, ky), v) for (kx, ky), v in data.items() if ky == endy]
            ys = [((kx, ky), v) for (kx, ky), v in data.items() if kx == endx]
            target = None
            if endd == 0:
                targets = sorted([x for x in xs if x[0][0] > endx], key=lambda p: p[0][0])
                if len(targets) > 0:
                    target = targets[0]
                else:
                    target = ((maxx, endy), '.')
            elif endd == 2:
                targets = sorted([x for x in xs if x[0][0] < endx], key=lambda p: p[0][0])
                if len(targets) > 0:
                    target = targets[-1]
                else:
                    target = ((0, endy), '.')
            elif endd == 1:
                targets = sorted([y for y in ys if y[0][1] > endy], key=lambda p: p[0][1])
                if len(targets) > 0:
                    target = targets[0]
                else:
                    target = ((endy, maxy), '.')
            elif endd == 3:
                targets = sorted([y for y in ys if y[0][1] < endy], key=lambda p: p[0][1])
                if len(targets) > 0:
                    target = targets[-1]
                else:
                    target = ((endy, 0), '.')

            targetP, targetV = target
            for dot in get_points_of_edge((endx, endy), targetP):
                energized.add(dot)

            if targetV != '.':
                targetd = dirchanges[(targetV, endd)]
                for d in targetd:
                    ends.append((targetP, d))

        for y in range(maxy):
            row = ''
            for x in range(maxx):
                if (x,y) in data.keys():
                   row += data[(x,y)]
                elif (x,y) in energized:
                    row += '#'
                else:
                    row += '.'
            print(row)

        return len(energized)
    
    def extended_task(self):
        pass


Task16()
