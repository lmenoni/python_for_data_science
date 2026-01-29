
from time import sleep

def ft_tqdm(lst: range):
    stamp:str = ""
    for i, x in enumerate(lst):
        perc = int((i + 1) * 100 / len(lst))
        n_of_equals = int(64 / 100 * perc)
        equals:str = "=" * n_of_equals
        spaces:str = " " * (64 - n_of_equals)
        # print(equals)
        print(f"\r{perc:3}% [{equals}{spaces}] {i}/{len(lst)}", end="", flush=True)
        yield x
    print("")

for x in ft_tqdm(range(333)):
    sleep(0.05)