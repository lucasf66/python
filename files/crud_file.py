import os
file1 = open('file1.txt')
file2 = open("file2.txt")
print(os.path.abspath(file1.name))
print(os.path.realpath(file2.name))
print(file1.read())
file1.close(); file2.close()


with open("file2.txt",'w') as file2:
    message = "linha1\rlinha2\rlinha3"
    file2.write(message)


def readLines(file):
    with open(file,"r") as file_read:
        for linha in file_read:
            print(linha)

readLines('file2.txt')

print(" \r\r------ proximo passo APPEND --------\r\r ")

def appendText(file,message):
    with open(file,"a") as file_write_append:
        file_write_append.write(f"\r{message}")

appendText('file2.txt','Funcinou!!!')

readLines('file2.txt')