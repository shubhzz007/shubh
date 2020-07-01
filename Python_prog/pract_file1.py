list = []
file = open("lissst.txt",'w')
file.write("1.shhhhh \n 2.djfkdjf \n 3.jsfdjf. \n 4.hsdhs. \n 5.jdnfjdfnj")
file = open("lissst.txt",'r')
print(file.read())
file = open("lissst.txt",'r')
for line in file:
    list.append(line)
    print(list)
