from PIL import Image

from tasks.abstracttask import AbstractTask


class Rock:

    def __init__(self, pos: (int, int), is_moving: bool) -> None:
        self.is_moving = is_moving
        self.current_pos = pos

    def move(self, x: int, y: int):
        self.current_pos = (x, y)


def toimage(path: str, height: int, width: int, rocks: [Rock]):
    rockmap = {(rock.current_pos[0], rock.current_pos[1]): rock for rock in rocks}
    img = Image.new('RGB', (width*2, height*2), "black")
    pixels = img.load()
    for idy in range(height):
        for idx in range(width):
            col = (0, 0, 0)
            if (idx, idy) in rockmap:
                rock = rockmap[(idx, idy)]
                col = (0, 255, 0) if rock.is_moving else (0, 0, 255)

            pixels[idx * 2, idy * 2] = col
            pixels[idx * 2 + 1, idy * 2] = col
            pixels[idx * 2, idy * 2 + 1] = col
            pixels[idx * 2 + 1, idy * 2 + 1] = col
    img.save(path)


def movenorth(width: int, height: int, squarerocks: [Rock], roundrocks: [Rock]):
    for column in range(width):
        sr = [x for x in squarerocks if x.current_pos[0] == column]
        current = 0
        last = height
        ranges = []
        for rock in sorted(sr, key=lambda x: x.current_pos[1]):
            ranges.append(range(current, rock.current_pos[1]))
            current = rock.current_pos[1] + 1
        ranges.append(range(current, last))

        for rockrange in ranges:
            for offset, rock in enumerate(sorted([x for x in roundrocks if
                                                  x.current_pos[0] == column and x.current_pos[
                                                      1] in rockrange], key=lambda x: x.current_pos[1])):
                rock.move(column, rockrange[0] + offset)

def movewest(width: int, height: int, squarerocks: [Rock], roundrocks: [Rock]):
    for row in range(height):
        sr = [x for x in squarerocks if x.current_pos[1] == row]
        current = 0
        last = width
        ranges = []
        for rock in sorted(sr, key=lambda x: x.current_pos[0]):
            ranges.append(range(current, rock.current_pos[0]))
            current = rock.current_pos[0] + 1
        ranges.append(range(current, last))

        for rockrange in ranges:
            for offset, rock in enumerate(sorted([x for x in roundrocks if
                                                  x.current_pos[1] == row and x.current_pos[0] in rockrange], key=lambda x: x.current_pos[0])):
                rock.move(rockrange[0] + offset, row)


def movesouth(width: int, height: int, squarerocks: [Rock], roundrocks: [Rock]):
    for column in range(width):
        sr = [x for x in squarerocks if x.current_pos[0] == column]
        current = 0
        last = height
        ranges = []
        for rock in sorted(sr, key=lambda x: x.current_pos[1]):
            ranges.append(range(current, rock.current_pos[1]))
            current = rock.current_pos[1] + 1
        ranges.append(range(current, last))

        for rockrange in ranges[::-1]:
            for offset, rock in enumerate(list(sorted([x for x in roundrocks if
                                                  x.current_pos[0] == column and x.current_pos[1] in rockrange], key=lambda x: x.current_pos[1]))[::-1]):
                rock.move(column, rockrange[-1] - offset)


def moveeast(width: int, height: int, squarerocks: [Rock], roundrocks: [Rock]):
    for row in range(height):
        sr = [x for x in squarerocks if x.current_pos[1] == row]
        current = 0
        last = width
        ranges = []
        for rock in sorted(sr, key=lambda x: x.current_pos[0]):
            ranges.append(range(current, rock.current_pos[0]))
            current = rock.current_pos[0] + 1
        ranges.append(range(current, last))

        for rockrange in ranges[::-1]:
            rr = list(sorted([x for x in roundrocks if x.current_pos[1] == row and x.current_pos[0] in rockrange], key=lambda x: x.current_pos[0]))[::-1]
            for offset, rock in enumerate(rr):
                rock.move(rockrange[-1] - offset, row)

def printcurrent(width: int, height: int, rocks: [Rock]):
    rockmap = {(rock.current_pos[0], rock.current_pos[1]): rock for rock in rocks}
    for idy in range(height):
        for idx in range(width):
            if (idx, idy) in rockmap:
                rock = rockmap[(idx, idy)]
                print('O' if rock.is_moving else '#', end='')
            else:
                print('.', end='')
        print('\n')
    print("\n")

def calcresult(length: int, positions: [(int, int)]):
    result = 0
    for rock in positions:
        result += (length - rock[1])
    return result


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
        roundrocks = [x for x in rocks if x.is_moving]
        movenorth(len(lines[0]), len(lines), squarerocks, roundrocks)

        result = calcresult(len(lines), [x.current_pos for x in roundrocks])
        return result

    def extended_task(self):
        lines = self.read_file_lines()
        rocks = []
        for idy, line in enumerate(lines):
            for idx, char in enumerate(line):
                if char != '.':
                    rocks.append(Rock((idx, idy), char == 'O'))

        squarerocks = [x for x in rocks if not x.is_moving]
        roundrocks = [x for x in rocks if x.is_moving]

        currentSet = set([x.current_pos for x in roundrocks])
        map = []
        idx = 0
        while currentSet not in map:
            map.append(currentSet)
            toimage(f"image/{idx:03d}_0.bmp", len(lines), len(lines[0]), rocks)
            movenorth(len(lines[0]), len(lines), squarerocks, roundrocks)
            toimage(f"image/{idx:03d}_1.bmp", len(lines), len(lines[0]), rocks)
            movewest(len(lines[0]), len(lines), squarerocks, roundrocks)
            toimage(f"image/{idx:03d}_2.bmp", len(lines), len(lines[0]), rocks)
            movesouth(len(lines[0]), len(lines), squarerocks, roundrocks)
            toimage(f"image/{idx:03d}_3.bmp", len(lines), len(lines[0]), rocks)
            moveeast(len(lines[0]), len(lines), squarerocks, roundrocks)
            currentSet = set([x.current_pos for x in roundrocks])

            idx += 1

        idx = map.index(currentSet)
        loop = len(range(idx, len(map)))
        togo = len(range(idx, 1000000000))
        finalpos = idx + (togo % loop)
        final = map[finalpos]

        result = calcresult(len(lines), final)
        return result


Task14()
