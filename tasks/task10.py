from tasks.abstracttask import AbstractTask


class Pipe():

    def __init__(self, char: str, pos: (int, int)) -> None:
        self.pos = pos
        self.char = char
        neighbors = {
            'u': (pos[0], pos[1] - 1),
            'l': (pos[0] - 1, pos[1]),
            'r': (pos[0] + 1, pos[1]),
            'd': (pos[0], pos[1] + 1)
        }
        chars = {
            '.': (),
            '7': ('l', 'd'),
            'J': ('l', 'u'),
            'F': ('r', 'd'),
            'L': ('r', 'u'),
            '|': ('d', 'u'),
            '-': ('r', 'l'),
            'S': ('r', 'l', 'd', 'u')
        }
        self.neighbors = [neighbors[x] for x in chars[char]]

    def isconnected(self, pipe):
        return self.pos in pipe.neighbors and pipe.pos in self.neighbors



class Task10(AbstractTask):
    def __init__(self):
        super().__init__(10)

    def simple_task(self):
        return ''
        lines = self.read_file_lines()
        map = {}
        start = None
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                pipe = Pipe(lines[y][x], (x, y))
                map[(x, y)] = pipe
                if pipe.char == 'S':
                    start = pipe.pos
        distances = [[start]]
        visited = [start]
        found = True
        while found:
            found = False
            newneighbors = []
            for pipe in [map[x] for x in distances[-1]]:
                neighbors = [n for n in pipe.neighbors if n not in visited and n in map.keys() and map[n].isconnected(pipe)]
                visited += neighbors
                newneighbors += neighbors
            if len(newneighbors) > 0:
                found = True
                distances.append(newneighbors)

        return len(distances) - 1


    def extended_task(self):
        lines = self.read_file_lines()
        map = {}
        start = None
        for y in range(len(lines)):
            for x in range(len(lines[y])):
                pipe = Pipe(lines[y][x], (x, y))
                map[(x, y)] = pipe
                if pipe.char == 'S':
                    start = pipe.pos
        distances = [[start]]
        visited = [start]
        # replace S sign
        startneighbors = tuple(set([(n[0] - start[0], n[1] - start[1]) for n in map[start].neighbors if n in map.keys() and map[n].isconnected(map[start])]))
        map[start].char = {
            ((-1, 0), (1, 0)): '-',
            ((-1, 0), (0, -1)): 'J',
            ((-1, 0), (0, 1)): '7',
            ((1, 0), (0, -1)): 'L',
            ((1, 0), (0, 1)): 'F',
            ((0, -1), (0, 1)): '|',
        }[startneighbors]

        found = True
        while found:
            found = False
            newneighbors = []
            for pipe in [map[x] for x in distances[-1]]:
                neighbors = [n for n in pipe.neighbors if
                             n not in visited and n in map.keys() and map[n].isconnected(pipe)]
                visited += neighbors
                newneighbors += neighbors
            if len(newneighbors) > 0:
                found = True
                distances.append(newneighbors)

        pipeline = set(visited)

        dots = []
        for y in range(len(lines)):
            inPipe = False
            for x in range(len(lines[0])):
                pos = (x, y)
                char = map[pos].char
                if pos in pipeline and char in '|F7':
                    inPipe = not inPipe
                elif pos not in pipeline and inPipe:
                    dots.append(pos)
        return len(dots)



Task10()