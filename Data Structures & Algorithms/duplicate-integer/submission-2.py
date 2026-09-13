class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        unique_elements = set()
        for i in nums :
            unique_elements.add(i)
 
        if len(nums)==len(unique_elements):
            return False 
        else:
            return True 
