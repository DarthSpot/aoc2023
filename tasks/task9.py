from tasks.abstracttask import AbstractTask


class Task9(AbstractTask):
    def __init__(self):
        super().__init__(9)

    def simple_task(self):
        lines = self.read_file_lines()
        values = [[int(y) for y in x.split()] for x in lines]
        result = 0
        for line in values:
            tmp = [line]
            while set(tmp[-1]) != {0}:
                tmp.append([tmp[-1][i+1] - tmp[-1][i] for i in range(len(tmp[-1])-1)])
            for row in range(len(tmp)-2, -1, -1):
                tmp[row].append(tmp[row][-1] + tmp[row+1][-1])
            result += tmp[0][-1]
        return result

    def extended_task(self):
        lines = self.read_file_lines()
        values = [[int(y) for y in x.split()] for x in lines]
        result = 0
        for line in values:
            tmp = [line]
            while set(tmp[-1]) != {0}:
                tmp.append([tmp[-1][i + 1] - tmp[-1][i] for i in range(len(tmp[-1]) - 1)])
            for row in range(len(tmp) - 2, -1, -1):
                tmp[row] = [(tmp[row][0] - tmp[row + 1][0])] + tmp[row]
            result += tmp[0][0]
        return result


Task9()