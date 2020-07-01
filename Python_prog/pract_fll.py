file = open("norm.txt",'w')
file.write("hello there\ni m in a sandip foundation\npython is a programming language\nhdsjdhsjdhsjdhsjdshdjh")
file = open("norm.txt",'r')
wrd1 = file.read().split( )
print(wrd1)
max = 0
longstr = ''
for wrd in wrd1:
    if len(wrd) > max:
        max = len(wrd)
        longstr = wrd
print(max)
print(longstr)
#    print(wrd)
#    wrd1 = wrd.read().split()
#print(wrd1)
flag = 0
cnttt = 0
key = input("enter the key to find the word :")
rep = input("enter word to replace the perticular word :")
#print(wrd1)
for i in range(0,len(wrd1)):
    if key == wrd1[i]:
        cnttt = cnttt + 1
#        flag = 1
        wrd1[i] = rep
if cnttt > 0:

    print("word is found ",cnttt," times")
    print(wrd1)
else:
    print("word is not found")


