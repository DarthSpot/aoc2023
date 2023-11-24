from tasks.abstracttask import AbstractTask


class Task_1(AbstractTask):
    
    def __init__(self):
        super().__init__(1)
        
    def simple_task(self):
        return self.read_file_lines()
    
    def extended_task(self):
        return self.read_file_string()
    
Task_1()
