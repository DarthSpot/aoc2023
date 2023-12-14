from tasks.abstracttask import AbstractTask


class Rock:

    def __init__(self, pos: (int, int), is_moving: bool) -> None:
        self.orig_pos = pos
        self.is_moving = is_moving
        self.current_pos = pos

    def move(self, x: int, y: int):
        self.current_pos = (x, y)


class Task14(AbstractTask):
    def __init__(self):
        super().__init__(14)

    def simple_task(self):
        lines = self.read_file_lines()
        rocks = []
        for idy, line in enumerate(lines):
            for idx, char in enumerate(line):
                if char != '.':
                    rocks.append(Rock((idx, idy), char == 'O'))

        squarerocks = [x for x in rocks if not x.is_moving]
        for column in range(len(lines[0])):
            sr = [x for x in squarerocks if x.orig_pos[0] == column]
            current = 0
            last = len(lines)
            ranges = []
            for rock in sorted(sr, key=lambda x: x.orig_pos[1]):
                ranges.append(range(current, rock.orig_pos[1]))
                current = rock.orig_pos[1] + 1
            ranges.append(range(current, last))

            for rockrange in ranges:
                for offset, rock in enumerate(sorted([x for x in rocks if x.is_moving and x.orig_pos[0] == column and x.orig_pos[1] in rockrange], key=lambda x: x.orig_pos[1])):
                    rock.move(column, rockrange[0] + offset)

        result = 0
        for rock in [x for x in rocks if x.is_moving]:
            result += (len(lines) - rock.current_pos[1])

        rockmap = {(rock.current_pos[0], rock.current_pos[1]):rock for rock in rocks}

        for idy, line in enumerate(lines):
            for idx, char in enumerate(line):
                if (idx,idy) in rockmap:
                    rock = rockmap[(idx,idy)]
                    print('O' if rock.is_moving else '#', end='')
                else: print('.', end='')
            print('\n')

        return result

    def extended_task(self):
        pass

Task14()