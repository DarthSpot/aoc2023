from math import prod, lcm

from tasks.abstracttask import AbstractTask

BROADCAST = 'roadcaster'


def do_the_task(lines: [str], extended: bool):
    rawdata = [line.split(' -> ') for line in lines]
    data = [((rawsource[0], rawsource[1:]), (rawtarget.split(', '))) for rawsource, rawtarget in rawdata]
    pulsemap = {s[1]: t for s, t in data}
    lastsignal = {s[1]: False for s, t in data}
    flipflops = [s[1] for s, _ in data if s[0] == '%']
    gates = {s[1]: {} for s, _ in data if s[0] == '&'}
    gkeys = set(gates.keys())
    for gate_key, _ in gates.items():
        for ds, dt in pulsemap.items():
            if gate_key in dt:
                gates[gate_key][ds] = False

    rxgates = gates[[gk for gk, gv in pulsemap.items() if "rx" in gv][0]]
    rxtimings = {}

    result = {True: 0, False: 0}
    button = 0
    while button < 1000 or extended:
        button += 1
        pulses = [(BROADCAST, False)]
        while len(pulses) > 0:
            pulse, signal = pulses.pop(0)
            result[signal] += 1
            if pulse in pulsemap:
                targets = pulsemap[pulse]
                send = False
                out = False
                if pulse in flipflops and not signal:
                    out = not lastsignal[pulse]
                    lastsignal[pulse] = out
                    send = True
                elif pulse in gates.keys():
                    out = not all(gates[pulse].values())
                    if extended and pulse in rxgates and pulse not in rxtimings.keys() and out:
                        rxtimings[pulse] = button
                    if len(rxtimings) == len(rxgates):
                        return lcm(*rxtimings.values())
                    send = True
                if send or pulse == BROADCAST:
                    for t in targets:
                        pulses.append((t, out))
                        if t in gkeys:
                            gates[t][pulse] = out

    return prod(result.values())

class Task20(AbstractTask):
    def __init__(self):
        super().__init__(20)

    def simple_task(self):
        lines = self.read_file_lines()
        return do_the_task(lines, False)


    def extended_task(self):
        lines = self.read_file_lines()
        return do_the_task(lines, True)


Task20()
