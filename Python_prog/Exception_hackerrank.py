n = int(input())
lst=[]
for i in range(n):
    a = list(map(str, input().split()))
    lst.append(a)
for j in lst:
    try:
        b = int(j[0])/int(j[1])
        print(int(b))
    except ZeroDivisionError as e:
        print("Error Code : integer division or modulo by zero")
    except ValueError as a:
        print("Error Code :", a)