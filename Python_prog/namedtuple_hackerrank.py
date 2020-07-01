from collections import namedtuple
lst = list(map(str, input().split()))
student = namedtuple('student',lst)
'''s = student(1,70,'abc', 'A')
print(s.NAME)'''
n = int(input())
for i in range(n):
    s = student(list(map(str, input().split())))
    #s[i] = student._make(li)
#for j in range(n):
    print(s)
#print(s1)