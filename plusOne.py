class Solution(object):
    def plusOne(self, digits):
       new_digits="".join(map(str,digits))
       incremented=int(new_digits)+1
       return [int(d) for d in str(incremented)] 
digits = [4,3,2,1]

result = Solution()
output = result.plusOne(digits)

print("The new array is:",output)    
