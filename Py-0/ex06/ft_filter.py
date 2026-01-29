
def ft_filter(function, iterable):
    res = [x for x in iterable if function(x)]
    return iter(res)


# def is_higher_than_zero(value:int):
#     return value > 0

# ns = [0, 1, 0, 2, 0, -1, 4, 2]
# no_zero = ft_filter(is_higher_than_zero, ns)

# print(ns)
# # print(no_zero)
# for n in no_zero:
#     print(n)