# make a table of ASCII values of upper and lower-case alphabet
# fileU.txt = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# fileL.txt = 'abcdefghijklmnopqrstuvwxyz'
file = open("fileL.txt")
while 1:
    char = file.read(1)
    if not char:
        break
    for i in char:
        print(i,":\t",ord(char))

