class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        check_val = {'(':')','{':'}','[':']'}

        for i in s:
            if i in check_val:
                stack.append(i)

            elif i in check_val.values() :
                if not stack or check_val[stack[-1]] != i:
                    return False
                stack.pop() 
            
            else:
                return False 
        return not stack