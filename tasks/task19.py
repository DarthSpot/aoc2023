import operator
import re

from tasks.abstracttask import AbstractTask

class Rule():
    def __init__(self, name: str, rules: [(str, operator, int, str)], other: str):
        self.name = name
        self.rules = rules
        if all([t == other for _, _, _, t in rules]):
            self.rules = {}
        self.other = other

    def __str__(self):
        return f'{self.name}: {self.rules} | {self.other}'

    def apply(self, partmap: {str: int}):
        for v, op, c, t in self.rules:
            if op(partmap[v], c):
                return t
        return self.other


class Task19(AbstractTask):
    def __init__(self):
        super().__init__(19)
    
    def simple_task(self):

        lines = """px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}"""
        lines = self.read_file_string()
        rawrules, rawdata = [x.split("\n") for x in lines.strip().split("\n\n")]
        rulebook = {}
        for rulesname, rules in [raw[:-1].split('{') for raw in rawrules]:
            ruledata = []
            other = rules.split(',')[-1]
            for raw in rules.split(',')[:-1]:
                rule, target = raw.split(':')
                ruledata.append((rule[0], operator.lt if rule[1] == '<' else operator.gt, int(rule[2:]), target))
            rulebook[rulesname] = Rule(rulesname, ruledata, other)

        result = []
        for parts in [x[1:-1].split(',') for x in rawdata]:
            partmap = {v: int(i) for v, i in [p.split('=') for p in parts]}
            wf = 'in'
            while wf not in 'AR':
                rb = rulebook[wf]
                wf = rb.apply(partmap)
            if wf == 'A':
                result.append(partmap)
        return sum([sum(x.values()) for x in result])

    
    def extended_task(self):
        pass


Task19()
