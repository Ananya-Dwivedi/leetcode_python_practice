class Solution(object):
    def containsDuplicate(self, nums):
        seen=set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)

        return False



if __name__ == "__main__":
    # nums = [1,2,3,4] 
    nums = [1,2,3,1] 
    solver = Solution()
    result = solver.containsDuplicate(nums)
    print(result)
   
