class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(word)}#{word}" for word in strs)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            separator = s.index("#", i)
            length = int(s[i:separator])
            start = separator + 1
            result.append(s[start:start + length])
            i = start + length

        return result