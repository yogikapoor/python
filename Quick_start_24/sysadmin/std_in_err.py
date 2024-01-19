#!/usr/bin/env python3
import sys

# print( "Hello, World")
# sys.stdout.write('Hello, world\n')
# print("error occured")
# sys.stderr.write("Error Occured\n")
# sys.stdout.write("Username: ")
# username = sys.stdin.readline()
# print(f"{username}")

# reading lines (separated by newlines) from stdin
print('Enter few lines and press Ctrl-D')
lines = sys.stdin.readlines()
print ('total lines read:', len(lines))