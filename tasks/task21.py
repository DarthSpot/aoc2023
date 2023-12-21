from collections import deque

from tasks.abstracttask import AbstractTask


def calc_result(values: [int], n: int):
    a0, a1, a2 = values
    b0 = a0
    b1 = a1 - a0
    b2 = a2 - a1
    return b0 + b1 * n + (n * (n - 1) // 2) * (b2 - b1)


class Task21(AbstractTask):
    def __init__(self):
        super().__init__(21)
    
    def simple_task(self):
        lines = self.read_file_lines()
        w = len(lines[0])
        h = len(lines)
        positions = set()
        for y, line in enumerate(lines):
            for x, c in enumerate(line):
                if c == 'S':
                    positions.add(((x, y), 0))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        visited = {}
        visiting = deque(positions)
        while len(visiting) > 0:
            pos, steps = visiting.popleft()
            if pos in visited.keys():
                continue
            if steps == 65:
                break
            visited[pos] = steps
            for direction in directions:
                new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                x, y = new_pos
                if 0 <= x < w and 0 <= y < h and lines[y][x] in '.S':
                    visiting.append((new_pos, steps + 1))

        return sum([1 - (v % 2) for v in visited.values()])


    def extended_task(self):
        lines = self.read_file_lines()
        positions = set()
        w = len(lines[0])
        h = len(lines)
        positions.add((w//2, h//2))
        max_steps = 26501365
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        steps = 0
        values = []
        max_step_mod = max_steps % h
        plen = 0
        while len(values) < 3:
            steps += 1
            current, positions = set(positions), set()
            for pos in current:
                for direction in directions:
                    new_pos = (pos[0] + direction[0], pos[1] + direction[1])
                    posx, posy = new_pos
                    if lines[posy % h][posx % w] in 'S.':
                        positions.add(new_pos)
            if steps % h == max_step_mod:
                print(steps, len(positions), len(positions) - plen)
                values.append(len(positions))
                plen = len(positions)

        return calc_result(values, max_steps // h)


Task21()
