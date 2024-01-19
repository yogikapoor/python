#!/bin/bash/python3
my_dict={}
print(my_dict,type(my_dict))
print(bool(my_dict))
# dict is Key: value
my_dict = {'fruit':'apple', 'animal': 'Dog', 1: 'one', 'two': 2}
print(my_dict['fruit'])
print(my_dict.get('apple')) # It will display none
#print(my_dict.['apple']) # it will throw an error, there is no Key with Apple
print(my_dict[1])
print(my_dict.values())
print(my_dict.keys())
print(my_dict.items())
print(my_dict.items())
my_dict.setdefault('fruits','oranges')
print(my_dict)
