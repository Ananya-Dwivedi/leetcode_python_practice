class Solution(object):
    def removeDuplicates(self, nums):
        slow=0
        for fast in range(1,len(nums)):
            if nums[fast]!=nums[slow]:
                slow+=1
                nums[slow]=nums[fast]


        return (slow+1)



if __name__ == "__main__": 
    result=Solution()
    nums=[1,1,2]
    output=result.removeDuplicates(nums)
    print(output)