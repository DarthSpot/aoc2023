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
        lines = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L""".split("\n")
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
                neighbors = [n for n in pipe.neighbors if
                             n not in visited and n in map.keys() and map[n].isconnected(pipe)]
                visited += neighbors
                newneighbors += neighbors
            if len(newneighbors) > 0:
                found = True
                distances.append(newneighbors)

        pipeline = set(visited)
        dots = [v for k,v in map.items() if v.char == '.']
        fields = 0
        for dot in dots:
            leftlen = len([p for p in [map[(x, dot.pos[1])] for x in range(dot.pos[0]-1, -1, -1)] if p.pos in pipeline and p.char != '-'])
            rightlen = len([p for p in [map[(x, dot.pos[1])] for x in range(dot.pos[0], len(lines[0]))] if p.pos in pipeline and p.char != '-'])
            uplen = len([p for p in [map[(dot.pos[0], y)] for y in range(dot.pos[1]-1, -1, -1)] if p.pos in pipeline and p.char != '|'])
            downlen = len([p for p in [map[(dot.pos[0], y)] for y in range(dot.pos[1], len(lines))] if p.pos in pipeline and p.char != '|'])
            if len([x for x in [leftlen, rightlen, uplen, downlen] if x % 2 == 0]) == 0:
                fields += 1
        return fields



Task10()