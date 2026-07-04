class Solution(object):
    def singleNumber(self, nums):
        result = 0
        for num in nums:    
            result ^= num
        return result

nums = [4,1,2,1,2]

result = Solution()
output = result.singleNumber(nums)
print("The single number of the array is:", output)
        


# def singleNumber(nums):
#     nums.sort()  # Sort the array first
#     for i in range(0, len(nums) - 1, 2):
#         if nums[i] != nums[i + 1]:
#             return nums[i]
#     return nums[-1]  # If the single number is at the end