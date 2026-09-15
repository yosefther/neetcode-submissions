class Solution:
    def isPalindrome(self, s: str) -> bool:
        k = re.sub(r'[^a-zA-Z0-9]', '', s ).lower()
        return k == k[::-1]