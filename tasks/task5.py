import re

from tasks.abstracttask import AbstractTask


class Task5(AbstractTask):
    def __init__(self):
        super().__init__(5)

    def simple_task(self):
        lines = self.read_file_string().split("\n\n")
        seeds = [int(x) for x in lines[0].split()[1:]]
        bigMap = []
        for elem in lines[1:]:
            tinyMap = []
            for line in elem.strip().split('\n')[1:]:
                nums = [int(x) for x in line.split()]
                tinyMap.append((nums[1], nums[0], nums[2]))
            bigMap.append(sorted(tinyMap, key=lambda mapping: mapping[0]))

        locations = []
        for seed in seeds:
            current = seed
            for elem in bigMap:
                matches = [x for x in elem if x[0] <= current]
                if len(matches) > 0:
                    match = matches[-1]
                    if match[0] <= current <= match[0] + match[2]:
                        current = current - match[0] + match[1]
            locations.append(current)
        return sorted(locations)[0]

    def extended_task(self):
        lines = self.read_file_string().split("\n\n")

        seeds = [int(x) for x in lines[0].split()[1:]]
        seedGroups = [range(seeds[i], seeds[i] + seeds[i+1]) for i in range(0, len(seeds), 2)]
        bigMap = []
        for elem in lines[1:]:
            tinyMap = []
            for line in elem.strip().split('\n')[1:]:
                nums = [int(x) for x in line.split()]
                tinyMap.append((range(nums[1], nums[1] + nums[2]), nums[0] - nums[1]))
            bigMap.append(sorted(tinyMap, key=lambda mapping: mapping[0][0]))

        location = None
        for seedGroup in seedGroups:
            currentGroup = [seedGroup]
            for elem in bigMap:
                newSplices = []
                for splice in currentGroup:
                    newSplices += self.createsplices(elem, splice)
                currentGroup = newSplices
            for rangeelem in currentGroup:
                if location is None or location > rangeelem[0]:
                    location = rangeelem[0]

        return location

    def createsplices(self, mapping: list[tuple[range, int]], group: range):
        grouprange = group
        hits = [x for x in mapping if len(self.overlap(x[0], grouprange)) > 0]
        slices = []
        for hit in sorted(hits, key=lambda x: x[0][0]):
            if grouprange[0] < hit[0][0]:
                slices.append(range(grouprange[0], hit[0][0]))
                grouprange = range(hit[0][0], grouprange[-1] + 1)

            diff = hit[1]
            overlap = self.overlap(hit[0], grouprange)
            slices.append(range(overlap[0] + diff, overlap[-1] + diff + 1))
            grouprange = range(overlap[-1] + 1, grouprange[-1] + 1)
        if len(grouprange) > 0:
            slices.append(grouprange)

        return [x for x in slices if len(x) > 0]

    def overlap(self, x: range, y: range):
        return range(max(x[0], y[0]), min(x[-1], y[-1]) + 1)


Task5()