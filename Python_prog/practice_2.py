class person:
    def __init__(d,first,last,pay):
        d.first = first
        d.last = last
        d.pay = pay
    def get(d):
        print("the name is :",end='')
        print(d.first + d.last)


p = person("sssss","abcds",9000)
p.get()
