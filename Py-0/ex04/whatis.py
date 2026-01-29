
import sys


def parse_arguments(args: list, argc: int) -> bool:
    if argc <= 0:
        return False

    if argc > 1:
        print("AssertionError: more than one argument is provided")
        return False

    arg = args[1]
    lenght = len(arg)
    for i in range(lenght):
        if arg[i] < '0' or arg[i] > '9':
            print("AssertionError: argument is not an integer")
            return False

    return True


def main():

    args = sys.argv
    argc = len(args) - 1

    if (not parse_arguments(args, argc)):
        return

    last_char = args[1][len(args[1]) - 1]
    if (ord(last_char) - 48) % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")


if __name__ == "__main__":
    main()
