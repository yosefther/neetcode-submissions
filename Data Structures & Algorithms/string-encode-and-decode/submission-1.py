class Solution:

    def encode(self, strs: List[str]) -> str:
        j = ""
        for i in range(len(strs)):
            j = str((j+"#@#$562"+strs[i]))
        return j
    def decode(self, s: str) -> List[str]:
        s=s.split("#@#$562")
             
        return s[1:]