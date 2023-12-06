import math

from tasks.abstracttask import AbstractTask

class Task6(AbstractTask):
    def __init__(self):
        super().__init__(6)

    def simple_task(self):
        input = [x.split()[1:] for x in self.read_file_lines()]
        games = [(int(input[0][i]), int(input[1][i])) for i in range(len(input[0]))]
        return math.prod([len([x for x in range(1, game[0]) if x * (game[0] - x) > game[1] ]) for game in games])

    def extended_task(self):
        input = [int(''.join(y)) for y in [x.split()[1:] for x in self.read_file_lines()]]
        min = math.ceil((input[0] - math.sqrt(input[0] * input[0] - 4 * input[1])) / 2)
        max = math.floor((input[0] + math.sqrt(input[0] * input[0] - 4 * input[1])) / 2)

        return max - min + 1



Task6()
