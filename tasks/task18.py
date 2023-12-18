from tasks.abstracttask import AbstractTask

def printmap(map):
    xpos = [x for x, y in map]
    xmin = min(xpos)
    xmax = max(xpos)
    ypos = [y for x, y in map]
    ymin = min(ypos)
    ymax = max(ypos)

    for y in range(ymin, ymax + 1):
        row = ''
        for x in range(xmin, xmax + 1):
            if (x,y) in map:
                row += '#'
            else:
                row += '.'
        print(row)

def crosses(points):
    if len(points) == 0:
        return False
    xs = sorted([x for x, y in points])
    groups = groupbyneighbor(xs)
    return len(groups) % 2 == 1

def groupbyneighbor(numbers):
    group = [numbers[0]]
    for idx, num in enumerate(numbers[1:]):
        if group[-1] == num - 1:
            group.append(num)
        else:
            return [group] + groupbyneighbor(numbers[idx + 1:])
    return [group]

class Task18(AbstractTask):
    def __init__(self):
        super().__init__(18)
    
    def simple_task(self):
        lines = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)""".split("\n")
        lines = self.read_file_lines()
        input = [line.split() for line in lines]
        pos = (0,0)
        dirs = {
            'R': (1, 0),
            'D': (0, 1),
            'U': (0, -1),
            'L': (-1, 0),
        }
        digged = [(0,0)]
        for dir, distance, col in input:
            dirm = dirs[dir]
            target_pos = (pos[0] + dirm[0] * int(distance), pos[1] + dirm[1] * int(distance))
            coords = []
            if target_pos[1] > pos[1]:
                for c in range(pos[1] + 1, target_pos[1] + 1):
                    coords.append((pos[0], c))
            elif target_pos[1] < pos[1]:
                for c in range(pos[1] - 1, target_pos[1] - 1, -1):
                    coords.append((pos[0], c))
            elif target_pos[0] > pos[0]:
                for c in range(pos[0] + 1, target_pos[0] + 1):
                    coords.append((c, pos[1]))
            elif target_pos[0] < pos[0]:
                for c in range(pos[0] - 1, target_pos[0] - 1, -1):
                    coords.append((c, pos[1]))
            for coord in coords:
                digged.append(coord)
            pos = target_pos

        result = set(digged)
        ys = [y for x, y in digged]
        xs = [x for x, y in digged]
        for yp in range(min(ys), max(ys) + 1):
            for xp in range(min(xs), max(xs) + 1):
                if (xp, yp) not in result:
                    left = [(x, y) for x, y in digged if y == yp and x < xp]
                    if crosses(left):
                        result.add((xp, yp))
        return len(result)
    
    def extended_task(self):
        pass


Task18()
