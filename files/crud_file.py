import os
file1 = open('file1.txt')
file2 = open("file2.txt")
print(os.path.abspath(file1.name))
print(os.path.realpath(file2.name))
print(file1.read())
file1.close(); file2.close()