class Solution(object):
    def isValid(self, s):
        pairs={')':'(','}':'{',']':'['}
        stack=[]
        for char in s :
            if char not in pairs:
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    top=stack.pop()
                    if pairs[char]!=top:
                        return False
        return True




if __name__ == "__main__": 
    result=Solution()
    s='(){][]}'
    
    output=result.isValid(s)
    print(output)  