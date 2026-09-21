class Solution:
    def isValid(self, s: str) -> bool:
        valid_dict = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []

        if len(s) % 2 != 0:
            return False

        for i in range(len(s)):
            if s[i] in valid_dict:                     
                stack.append(s[i])
            else:                                      
                if len(stack) == 0:                    
                    return False
                top = stack.pop()
                if valid_dict[top] != s[i]:            
                    return False

        return len(stack) == 0
