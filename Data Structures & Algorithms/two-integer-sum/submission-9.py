class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for index , num in enumerate(nums):
            rem = target - num
            if rem in seen :
                return [ seen[rem] , index]
            seen [num]= index 