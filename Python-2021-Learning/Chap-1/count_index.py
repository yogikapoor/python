my_str = "python is easy and it is popular language"
print(my_str.count('is'))
print(my_str.count('easy'))
print(my_str.index('p'))
print(my_str.index('p',20)) # searching letter 'p' after index value 20 
print(my_str.index('is',10))
print(my_str.find('p',30)) # if its not found, result will be -1
print(my_str.find('z')) # Coz we don't have 'z' letter it will result -1

