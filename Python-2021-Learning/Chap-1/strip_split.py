x = "Pppython"
print(x)
print(x.strip()) # strip will remove the space on left or right of the given variable
print(x.strip('p')) # starting of a variable
print(x.strip('n')) # it remove the 'n' from end of the string
print(x.lower().strip('p')) # it will conver the varible to lower and strip the pppp's
y = "python scripting is easy"
print(y.strip('easy'))
print(y.lstrip('python'))

z = "python./i"
print(z.strip('./i'))
print(y.rstrip('is easy').lstrip('python'))
print(y.split())

print(y.split('is'))