class Solution(object):
    def isAnagram(self, s, t):
        freq_s={}
        freq_t={}
        for i in range(len(s)):
            freq_s[s[i]]=freq_s.get(s[i],0)+1
            freq_t[t[i]]=freq_t.get(t[i],0)+1

        if freq_s==freq_t:
            return True
        return False



if __name__ == "__main__":
    s = "anagram"
    t = "nagaram"
    solver = Solution()
    result = solver.isAnagram(s,t)
    print(result)
   
