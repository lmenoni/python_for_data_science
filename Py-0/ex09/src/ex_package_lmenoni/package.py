

def add_one(nbr:int) -> int:
    return nbr + 1

def count_in_list(lst:list, obj) -> int:
    count = 0
    for x in lst:
        if type(x) == type(obj) and x == obj:
            count += 1
    return count