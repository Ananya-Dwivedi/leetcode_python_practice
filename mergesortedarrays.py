
class solution(object):
    def merge_sorted_array(self,nums1,m,nums2,n):
     
        p1 = m - 1          # Pointer for nums1's valid elements
        p2 = n - 1          # Pointer for nums2
        p = m + n - 1       # Pointer for placement in nums1

        # Merge from the end
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

        # If nums2 still has elements, copy them
        nums1[:p2 + 1] = nums2[:p2 + 1]


nums1 = [1,2,3,0,0,0]
m=3
nums2=[2,5,6]
n=3

obj=solution()
result=obj.merge_sorted_array(nums1,m,nums2,n)
print(result)
