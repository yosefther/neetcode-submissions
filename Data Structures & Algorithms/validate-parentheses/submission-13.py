class Solution:
    def isValid(self, s: str) -> bool:
        opening_parentheses={'{' , '[' , '('}
        parentheses_map={'}':'{' , ']':'[' , ')':'('}
        stack = []
        for c in s :
            if c in opening_parentheses:
                stack.append(c)
            else:
                if not stack or stack[-1] != parentheses_map[c]:
                    return False 
                stack.pop()
        return not stack  
