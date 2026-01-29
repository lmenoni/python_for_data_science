
PREFIXES = {list:"List : ", tuple:"Tuple : ", set:"Set : ", dict:"Dict : ", str:" is in the kitchen : "}

def all_thing_is_obj(object: any) -> int:
    c_type = type(object)

    if c_type is str:
        print(f"{object.capitalize()}{PREFIXES[c_type]}{c_type}")
    elif c_type in PREFIXES:
        print(f"{PREFIXES[c_type]}{c_type}")
    else :
        print("Type not found")

    return 42