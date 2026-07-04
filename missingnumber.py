


class Solution(object):
    def missingNumber(self, nums):
       for i in range(len(nums)+1):
            if i not in nums:
                return i
num2=[3,0,1]
result=Solution()
output=result.missingNumber(num2)
print(output)
