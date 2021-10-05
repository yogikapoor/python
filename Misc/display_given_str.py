import os
t_width = os.get_terminal_size().columns
given_str = input("Enter your string value: " )
print(f"{given_str.center(t_width)}")
print(f"{given_str.ljust(t_width)}")
print(f"{given_str.title()}")