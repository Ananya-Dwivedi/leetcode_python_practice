class Solution(object):
    def removeStars(self, s):
        seen=[]
        for i in s:
            if i.isalnum():
                seen.append(i)
            else:
                seen.pop()
        ans=''.join(seen)
        return ans





if __name__ == "__main__": 
    result=Solution()
    s = "leet**cod*e"
    
    output=result.removeStars(s)
    print(output)          