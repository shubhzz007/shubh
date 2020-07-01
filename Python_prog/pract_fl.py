file = open("xyz.txt",'w')
file.write("hello\nthere is a data\ndhawal is a boy\nhi sandip foundation")
file = open("xyz.txt",'r')
list = file.read().split()
print(list)
cnt: int = 0
for i in list:
    print(i)
    cnt = cnt + 1

print("number of words are : :",cnt)

file = open("xyz.txt",'r')
cntt: int = 0
for line in file:
    print(line)
    cntt = cntt + 1
print("number of lines are :",cntt)