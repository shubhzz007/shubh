class Solution:
    def twoSum(self, nums, target):
        for i in nums:
            for j in nums:
                if i==j:
                    pass
                if target==i+j:
                    res =[i,j]
                    return res

s =  Solution()
nums = list(map(int, input().split()))
target = int(input())
print(s.twoSum(nums, target))