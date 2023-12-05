import sys
import time

from tasks import *
from tasks.abstracttask import AbstractTask


def main():
    if len(sys.argv) != 2:
        print('Usage: python main.py <Task Number>')
        sys.exit(1)
    try:
        number = int(sys.argv[1])
        task = AbstractTask.instances.get(number, None)
        if task is None:
            print(f"Task #{number} is not implemented yet")
        else:
            print(f"Task #{number}")
            print("Simple:")
            start = time.time()
            print(task.simple_task())
            end = time.time()
            print("Elapsed: {elapsed:.5f}".format(elapsed=end - start))
            print("Extended:")
            start = time.time()
            print(task.extended_task())
            end = time.time()
            print("Elapsed: {elapsed:.5f}".format(elapsed=end - start))

    except ValueError:
        print('Error: Argument must be an integer.')
        sys.exit(1)


if __name__ == "__main__":
    main()
    