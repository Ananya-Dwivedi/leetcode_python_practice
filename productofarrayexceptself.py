class Solution(object):
    def productExceptSelf(self, nums):
        answer=[1]*len(nums)
        prefix=1
        for i in range(len(nums)):
            answer[i]=prefix
            prefix=prefix*nums[i]
        suffix=1
        for i in range(len(nums)-1,-1,-1):
            answer[i]*=suffix
            suffix*=nums[i]
        return answer

if __name__ == "__main__": 
    result=Solution()
    nums=[1,2,3,4]
    
    output=result.productExceptSelf(nums)
    print(output)                