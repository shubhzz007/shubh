a = 10
def something():
    a = 9
    print(a)
    a = 30
    print(a)
    x = globals()['a']
    a = 20
    print("x is ",x)

    print("inside function :",a)


something()
print("outside :",a)