
import sys

NESTED_MORSE = { ' ': '/', 'A': '.—', 'N': '—.', '0': '—————', '.': '.—.—.—', 'B': '—...', 'O': '———', '1': '.————', ',': '——..——', 'C': '—.—.', 'P': '.——.', '2': '..———', ':': '———...', 'D': '—..', 'Q': '——.—', '3': '...——', '?': '..——..', 'E': '.', 'R': '.—.', '4': '....—', '=': '—...—', 'F': '..—.', 'S': '...', '5': '.....', '-': '—....—', 'G': '——.', 'T': '—', '6': '—....', '(': '—.——.', 'H': '....', 'U': '..—', '7': '——...', ')': '—.——.—', 'I': '..', 'V': '...—', '8': '———..', '"': '.—..—.', 'J': '.———', 'W': '.——', '9': '————.', "'": '.————.', 'K': '—.—', 'X': '—..—', '/': '—..—.', 'L': '.—..', 'Y': '—.——', 'M': '——', 'Z': '——..', '@': '.——.—.', '!': '—.—.——'}


def main():
    av = sys.argv
    ac = len(av) - 1

    if (ac != 1):
        print("AssertionError: Only one argument for call is accepted.")
        return
    
    s:str = av[1]
    res:str = ''

    for i, c in enumerate(s):
        if i > 0:
            res += " "
        c = c.capitalize()
        if (c not in NESTED_MORSE):
            print(f"AssertionError: {c} is an unkown caracter.")
            return
        res += NESTED_MORSE[c]
    
    print(res)




if __name__ == "__main__":
    main()