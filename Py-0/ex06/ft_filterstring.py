
from ft_filter import ft_filter
import sys


def main():
    argv = sys.argv
    argc = len(argv) - 1
    if argc != 2:
        print("AssertionError: the arguments are bad")
        return


    try:
        string = argv[1]
        words = string.split(' ')
        max_len = int(argv[2])

        iterator = ft_filter(lambda s : len(s) >= max_len, words)
        res = [x for x in iterator]
        print(res)

    except Exception:
        print("AssertionError: the arguments are bad")
    
    



if __name__ == "__main__":
    main()