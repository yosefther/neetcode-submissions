class Solution:
    def findMin(self, nums: list[int]) -> int:
        right = len(nums) - 1 
        left = 0  
        if nums[left] < nums[right] :
            return nums[left]
        while left < right:
                mid = (left+right)//2
                if nums[mid] > nums[right]:
                    left = mid+1 
                else :
                    right = mid 

        return nums[left]
        