import sys


def score(c: str) -> tuple:
    if c.isupper():
        return (1, 0, 0, 0, 0)
    elif c.islower():
        return (0, 1, 0, 0, 0)
    elif c.isdigit():
        return (0, 0, 0, 0, 1)
    elif c in ' \n\r':
        return (0, 0, 0, 1, 0)
    elif c in ';:,.!?-':
        return (0, 0, 1, 0, 0)
    return (0, 0, 0, 0, 0)


def main():
    argv = sys.argv
    argc = len(argv)
    if argc > 2:
        print("AssertionError: too many arguments")
        return

    if argc == 1:
        print("What is the text to count?")
        s = sys.stdin.readline()
        # s = input("What is the text to count?\n")
    else:
        s = argv[1]

    values = [0, 0, 0, 0, 0]

    for c in s:
        score_result = score(c)
        values = [values[i] + score_result[i] for i in range(5)]

    print(f"The text contains {len(s)} characters:")
    print(f"{values[0]} upper letters")
    print(f"{values[1]} lower letters")
    print(f"{values[2]} punctuation marks")
    print(f"{values[3]} spaces")
    print(f"{values[4]} digits")



if __name__ == "__main__":
    main()