import sys

from tasks.task_1 import *

def main():
    if len(sys.argv) != 2:
        print('Usage: python main.py <integer>')
        sys.exit(1)
    try:
        task = AbstractTask.instances[int(sys.argv[1])]
        print(f"Task #{task.number}")
        print("Simple:")
        print(task.simple_task())
        print("Extended:")
        print(task.extended_task())
        
        
        
    except ValueError:
        print('Error: Argument must be an integer.')
        sys.exit(1)


if __name__ == "__main__":
    main()
