import sys
from os import path

def main():
    if len(sys.argv) != 2:
        print('Usage: python gentask.py <Task Number>')
        sys.exit(1)
    try:
        number = int(sys.argv[1])
        fn = f"task{number}.py"
        tn = f"Task{number}"
        folder = "tasks"
        importline = f"from tasks.task{number} import {tn}\n"
        file = path.join(folder, fn)
        if not path.exists(file):
            f = open(file, 'w')
            f.write(f"""from tasks.abstracttask import AbstractTask


class {tn}(AbstractTask):
    def __init__(self):
        super().__init__({number})
    
    def simple_task(self):
        pass
    
    def extended_task(self):
        pass


{tn}()
""")
            f.close()

        initfile = open(path.join(folder, "__init__.py"), 'r')
        lines = initfile.readlines()
        initfile.close()
        if importline not in lines:
            initfile = open(path.join(folder, "__init__.py"), 'a')
            initfile.write(importline)
            initfile.close()


    except ValueError:
        print('Error: Argument must be an integer.')
        sys.exit(1)


if __name__ == "__main__":
    main()
