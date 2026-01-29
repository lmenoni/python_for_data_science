
ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list[1] = "World!"

# not mutable, safety reasons, works like a const value, you CAN'T do tuple[1] = someth
ft_tuple = ("Hello", "Italy!")

ft_set = {"Hello", "Florence!"}

ft_dict["Hello"] = "42Florence!"


print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)