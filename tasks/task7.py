import functools
import math

from tasks.abstracttask import AbstractTask
from collections import Counter


def translate(c, extended):
    if c.isnumeric():
        return int(c)
    return {
        "T": 10,
        "J": 1 if extended else 11,
        "Q": 12,
        "K": 13,
        "A": 14
    }[c]


def compare(a, b, extended):
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    for c in range(len(a[1])):
        va = translate(a[1][c], extended)
        vb = translate(b[1][c], extended)
        if va < vb:
            return -1
        elif va > vb:
            return 1
    return 0

class Task7(AbstractTask):
    def __init__(self):
        super().__init__(7)

    def simple_task(self):
        lines = self.read_file_lines()
        hands = [(self.get_score(hand), hand, int(bid)) for hand, bid in [x.split() for x in lines]]
        orderedHands = sorted(hands, key=functools.cmp_to_key(lambda a, b: compare(a, b, False)))
        return sum([(idx + 1) * int(x[2]) for idx, x in enumerate(orderedHands)])


    def get_score(self, hand):
        counter = Counter(hand)
        highest = max(counter.values())
        if highest == 5:
            return 7
        elif highest == 4:
            return 6
        elif len(counter) == 2:
            return 5
        elif highest == 3:
            return 4
        elif len(counter) == 3:
            return 3
        elif highest == 2:
            return 2
        else:
            return 1

    def get_score_ex(self, hand):
        if hand == 'JJJJJ':
            return 7
        count = dict(Counter(hand))
        mostcommon = max([(k,v) for k,v in count.items() if k != 'J'], key=lambda x: x[1])[0]
        newHand = hand.replace('J', mostcommon)
        return self.get_score(newHand)

    def extended_task(self):
        lines = self.read_file_lines()
        hands = [(self.get_score_ex(hand), hand, int(bid)) for hand, bid in [x.split() for x in lines]]
        orderedHands = sorted(hands, key=functools.cmp_to_key(lambda a, b: compare(a, b, True)))
        return sum([(idx + 1) * int(x[2]) for idx, x in enumerate(orderedHands)])

Task7()

