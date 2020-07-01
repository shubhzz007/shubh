def add_sub(x, y):
    d = x + y
    e = x - y
    return d, e

x = int(input("Enter number 1 :"))
y = int(input("Enter number 2 :"))
res1, res2 = add_sub(x, y)
print(res1, res2)
