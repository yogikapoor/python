import os
col1 = os.get_terminal_size().columns
given_str = input ("Enter any string  : ")
print(f"{given_str}")
print(given_str.center(col1))
print(given_str.ljust(col1))
print(given_str.rjust(col1))