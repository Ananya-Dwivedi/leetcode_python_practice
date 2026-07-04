

class Solution(object):
    def moveZeroes(self, nums):
        k=0
        for i in range(len(nums)):
            if nums[i]!=0:
                
                 nums[k]=nums[i]
               
                 k+=1

        for i in range(k,len(nums)):
            nums[i]=0 
        return nums

num2=[0,1,0,4,7,0,5,3,12]
# num2=[1,2,3,4,5,0,0,12,0]
# num2=[0,1,0,3,12]
result=Solution()
output=result.moveZeroes(num2)
print(output)
    