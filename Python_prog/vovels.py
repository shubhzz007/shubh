line = input("enter string :")
#vov=[]
#con=[]
vov1 = set()
con1 = set()
for i in line:
    if i == 'a' or i=='e' or i=='i' or i=='o' or i=='u':
        #if i not in vov1:
         #   #vov.append(i)
          #  vov1=i
        for key in range(0,len(line)):
            vov1.add(i)
    else:
       # if i not in con1:
           # #con.append(i)
            #con1=i
        con1.add(i)

print("vowels are :",vov1)


print("Consonent are :",con1)
#for i in range(0,len(line)):
 #   if line[i]==''