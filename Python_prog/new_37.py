def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i%2==0:
            even = even + 1
        else:
            odd = odd + 1
    return even,odd


lst = [2, 3, 4, 5, 67, 9, 986, 5, 4]
even,odd = count(lst)




print("even is :{} and odd is :{}".format(even,odd))