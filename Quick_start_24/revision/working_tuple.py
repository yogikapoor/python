#!/bin/bash/python3
my_empty=()
my_tuple=(3,4,5,'abc','hello',45)
print(my_tuple)
print(my_tuple[2])
print(my_tuple.count(3))
# tuple and stings ares immutable 
print(my_tuple[1:])

x=5,6,8,10 # it will also tuple, if you use commas in a variable assignments
print(type(x), x)
