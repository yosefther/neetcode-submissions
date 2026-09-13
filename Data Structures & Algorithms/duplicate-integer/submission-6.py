class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:            
                return True if len(set(nums)) != len(nums) else False