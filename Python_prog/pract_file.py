import os
file = open("ab.txt","w")
file.write("hello\nthere\nhiiiii how are you\ni m fine....!")
file = open("ab.txt","r")
for lst in file:
    print(file.read())
file = open("ab.txt","r")
n = int(input("enter the last numbers of lines you want to print :"))
print(file.readlines()[-n:])
