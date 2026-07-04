class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        pos_unique = 0
        for next_num in range(1, len(nums)):
            if nums[pos_unique] != nums[next_num]:
                pos_unique += 1
                nums[pos_unique] = nums[next_num]

        return pos_unique + 1  # Number of unique elements

# Usage
nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result = Solution()
output = result.removeDuplicates(nums)
print(f"The unique numbers are {output} and the array is {nums[:output]}")
