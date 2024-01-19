#!/bin/bash/python3

mylist=[1,3,4,6,5,7,8,5,100]
print(mylist.index(7)) # how to find seven index value
print(mylist[7]) # how to find data/value of 7th index 
print(mylist.count(5)) # counting how many times 5 value is in the list
#starting index of data 5
#mylist.clear() # deleting or clearing the list
x=mylist # only memory location will be copied
new_mylist = mylist.copy() 
print(new_mylist, id(mylist), id(new_mylist), id(x))
# mylist.append
# mylist.extend
# mylist.insert(1,33)
# mylist.remove(6)
mylist.pop() # It will remove the last index data
new_mylist.sort()


