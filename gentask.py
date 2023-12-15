import sys

def main():
    if len(sys.argv) != 2:
        print('Usage: python gentask.py <Task Number>')
        sys.exit(1)
    try:
        number = int(sys.argv[1])


    except ValueError:
        print('Error: Argument must be an integer.')
        sys.exit(1)


if __name__ == "__main__":
    main()