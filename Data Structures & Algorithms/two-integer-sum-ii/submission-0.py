class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(numbers)):
            seen[numbers[i]] = i  
        for i in range(len(numbers)):
            compl = target - numbers[i] 
            if compl in seen and seen[compl] != i  :
                return [i +1, seen[compl]+1]