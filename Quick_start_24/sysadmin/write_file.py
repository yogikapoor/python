#!/usr/bin/python3 
r = open('/etc/passwd1', 'r')
passwd = r.readlines()
for line in passwd:
    line = line.strip()
    size = len(line)
    print(size, line)
r.close()


with open('/etc/passwd1') as f:
    pass

w = open('test.txt', 'w')
w.write('127.0.0.1\n')
w.flush()
lines = ['1.1.1.1\n', '2.2.2.2\n', '3.3.3.3\n']
w.writelines(lines)
w.close()