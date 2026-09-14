class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        t1 = sorted(t)
        s2 = sorted(s)
        if s2 == t1:
            return True 
        else:
            return False 
