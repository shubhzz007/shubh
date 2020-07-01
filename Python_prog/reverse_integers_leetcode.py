class Solution:
    def reverse(self, x: int) -> int:
        lst = []
        lst.append(x)
        op = list(map(str, str(lst[0])))
        if op[0]=='-':
            op.remove("-")
            ls = op[::-1]
            print("-",end="")
            if ls[0]==0:
                ls.remove(0)
            for i in ls:
                print(int(i),end="")
        else:

            ls1 = op[::-1]
            if ls1[0]==0:
                ls1.remove(0)
            for i in ls1:
                print(int(i),end="")

s = Solution()
x = input()
s.reverse(x)