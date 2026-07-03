
class Solution(object):
    def twoSum(self, nums, target):
        seen = {}  # Dictionary to store number:index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i



# Example usage
if __name__ == "__main__":
    nums = [2, 7, 11, 15] 
    target = 9
    solver = Solution()
    result = solver.twoSum(nums, target)
    print("Indices of numbers that add up to target:", result)

# BRUTE FORCE

#  class Solution(object):
#     def twoSum(self, nums, target):
     
#         for i in range(0,len(nums)):
#             for j in range(0,len(nums)):
                
#                 if((nums[i]+nums[j]==target) and i!=j):        
#                     return [i,j]
                   
# nums=[2,7,11,15]
# target=9
# Add_Sum=Solution()
# print(Add_Sum.twoSum(nums,target))   