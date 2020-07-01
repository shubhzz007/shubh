# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations

lst = list(map(str, input().split()))
ln = int(lst[-1])
lst.pop()
st = set()
for i in lst:
    name = i
# print(ln)
for i in list(permutations(name, ln)):
    print(i)
