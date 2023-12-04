import re

from tasks.abstracttask import AbstractTask


class Task4(AbstractTask):
    def __init__(self):
        super().__init__(4)

    def simple_task(self):
        lines = self.read_file_lines()
        scans = [re.match(r"Card\s+(\d+): ([ \d]+) \| ([ \d]+)", x) for x in lines]
        values = [(re.findall(r"\d+", scan[3]), re.findall(r"\d+", scan[2])) for scan in scans]
        scores = [len({int(x) for x in scan[0]}.intersection({int(x) for x in scan[1]})) for scan in values]
        x = sum([pow(2, x-1) for x in scores if x > 0])
        return x


    def extended_task(self):
        lines = self.read_file_lines()
        scans = [re.match(r"Card\s+(\d+): ([ \d]+) \| ([ \d]+)", x) for x in lines]
        values = [(scan[1], re.findall(r"\d+", scan[3]), re.findall(r"\d+", scan[2])) for scan in scans]
        scores = [(value[0], len({int(x) for x in value[1]}.intersection({int(x) for x in value[2]}))) for value in values]
        cards = {int(score[0]): 1 for score in scores}
        for score in scores:
            game = int(score[0])
            wins = score[1]
            if wins > 0:
                targetRange = list(range(game+1, game + wins + 1))
                for win in targetRange:
                    cards[win] += cards[game]

        return sum(cards.values())


Task4()