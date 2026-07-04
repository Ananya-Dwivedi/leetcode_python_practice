class Solution(object):
    def groupAnagrams(self, strs):
        group={}
        for i in range(len(strs)):

            group_key=''.join(sorted(strs[i]))
            if group_key not in group:
                group[group_key]=[]
            group[group_key].append(strs[i])


        return list(group.values())
                
       



if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    solver = Solution()
    result = solver.groupAnagrams(strs)
    print(result)
       