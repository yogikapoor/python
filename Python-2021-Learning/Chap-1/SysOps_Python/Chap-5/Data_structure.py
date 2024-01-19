"""
my_list = []
my_list1 = [3, 2, 4, "python", 5.6]

print(bool(my_list))
print(bool(my_list1))
print(my_list1[3])
print(my_list1[3][1:])
my_list1[0]=45 # list are mutables 
print(my_list1)
#my_list1[3] = 2024
#print(my_list1)
print(type(my_list1))
old_str = "Python"
new_len = len(old_str)
print(new_len)
len_str = my_list1[3]
print(f' Here is the length of the string: {len(len_str)} ')
print(old_str.capitalize())
print(f' {old_str.upper()} {old_str.lower()} {old_str.title()}')
print(old_str.startswith('Py'))
print(old_str.endswith('n'))
print(old_str.istitle())

'''
my_list = [3, 5, 2, 7, 8, 5, 9]

# print(my_list.index(5,2))
# print(my_list.count(5))
# print(my_list)
# my_list.clear()
# print(my_list)
# my_new_list = my_list
# my_one_list = my_list.copy()
# print(id(my_list), id(my_new_list))
# print(id(my_one_list))
my_new_list = [56,45]
my_list.extend(my_new_list)
print(my_list)
my_list.remove(5)
print(my_list)

print(my_list)
#my_list.pop(0)
my_list.sort(reverse=True)
print(my_list)
"""

# #x = ['Py','th','on']
# print(x)
# print(x[0].strip(':'))
# print('Hello'.join(x[0]))

# my_list = [3, 5, 2, 7, 8, 5, 9]
# print(my_list.count(2,5))
x = " Hello World, Welcome to Python"
print(x.find('W',8))
print(x.find('W'))



