def fun(a, **b):
    print(a)
    for i,j in b.items():
        print(i,j)



fun("shubh",age=28, city='mumbai', mob=9897878)