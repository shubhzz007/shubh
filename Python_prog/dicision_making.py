x = int(input("enter the number :"))
y = int(input("Enter the second number :"))
if x > y:
    print("the {} is greater than {}".format(x,y))
elif x == y:
    print("the {} is equals to {}".format(x,y))
else:
    print("the {} is greater than {}".format(y,x))
