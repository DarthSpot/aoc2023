import math

from tasks.abstracttask import AbstractTask


class Task_2(AbstractTask):

    def __init__(self):
        super().__init__(2)

    def is_valid_game(self, turns):
        max = {'b': 14, 'g': 13, 'r': 12}
        for turn in turns:
            for pick in [x.strip().split(' ') for x in turn]:
                col = pick[1][0]
                val = int(pick[0])
                if max[col] < val:
                    return False
        return True


    def simple_task(self):
        games = self.read_file_lines()
        result = 0
        for game in [game.split(':') for game in games]:
            id = int(game[0].split(' ')[1])
            rounds = [turn.split(',') for turn in game[1].split(';')]
            if self.is_valid_game(rounds):
                result += id
        return result

    def extended_task(self):
        games = self.read_file_lines()
        result = 0
        for game in [game.split(':') for game in games]:
            dic = {'g': 0, 'b': 0, 'r': 0}
            id = int(game[0].split(' ')[1])
            rounds = [[x.strip().split(' ') for x in turn.split(',')] for turn in game[1].split(';')]
            for turn in rounds:
                for pick in turn:
                    col = pick[1][0]
                    val = int(pick[0])
                    if dic[col] < val:
                        dic[col] = val
            result += math.prod(dic.values())
        return result


Task_2()
