from tasks.abstracttask import AbstractTask


class Task1(AbstractTask):

    def __init__(self):
        super().__init__(1)

    def calculate_num(self, rows):
        result = 0
        for line in rows:
            filtered = list(filter(lambda c: c.isdigit(), line))
            num = int(''.join([filtered[i] for i in (0, -1)]))
            result += num
        return result

    def simple_task(self):
        return self.calculate_num(self.read_file_lines())

    def extended_task(self):
        rows = [self.get_numbers_from_text(x) for x in self.read_file_lines()]
        return self.calculate_num(rows)

    def get_numbers_from_text(self, text):
        numberNames = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        result = []
        for pos in range(len(text)-1):
            if text[pos].isdigit():
                result.append(text[pos])
            else:
                matches = [(text[pos:len(text)-1].startswith(x), str(idx+1)) for idx, x in enumerate(numberNames)]
                match = [x[1] for x in matches if x[0] is True]
                if len(match) != 0:
                    result.append(match[0])
        return ''.join(result)


Task1()
