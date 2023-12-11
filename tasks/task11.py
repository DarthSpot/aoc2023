import math

from tasks.abstracttask import AbstractTask


def calculate_galaxy(lines, extended: bool):
    emptyrows = [idx for idx, line in enumerate(lines) if set(line) == {'.'}]
    emptycols = [col for col in range(len(lines[0])) if set([x[col] for x in lines]) == {'.'}]
    map = []
    size = 1000000 if extended else 2
    y = 0
    for idy, row in enumerate(lines):
        x = 0
        for idx, col in enumerate(row):
            if col == '#':
                map.append((x, y))
            x += size if idx in emptycols else 1
        y += size if idy in emptyrows else 1

    pairs = []
    for idx in range(len(map)):
        for elem in map[idx + 1::]:
            pairs.append((map[idx], elem))

    distances = [(abs(b[0] - a[0]) + abs(b[1] - a[1])) for a, b in pairs]
    return sum(distances)


class Task11(AbstractTask):
    def __init__(self):
        super().__init__(11)

    def simple_task(self):
        lines = self.read_file_lines()
        return calculate_galaxy(lines, False)

    def extended_task(self):
        lines = self.read_file_lines()
        return calculate_galaxy(lines, True)


Task11()
