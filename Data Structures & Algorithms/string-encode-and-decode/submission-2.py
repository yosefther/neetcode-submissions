class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        j = ""
        for i in range(len(strs)):
            j = str((j+"#@#$562"+strs[i]))
        return j
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        s=s.split("#@#$562")
        return s[1:]