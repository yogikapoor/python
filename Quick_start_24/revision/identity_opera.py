#!/usr/bin/bash/python3
x = 6; y = 'Hello'; z = " world"

result = (type(x) is type(y))

print ( f' {result} ')
print( f' {type(y) is type(z)} ') 
print( f' {type(x) is not type(z)}')

x_list = []