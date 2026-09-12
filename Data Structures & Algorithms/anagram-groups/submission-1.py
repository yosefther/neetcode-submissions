class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict={}
        for i in strs :
            j = "".join(sorted(i.lower())) 
            my_dict.setdefault(j,[]).append(i)
        return list(my_dict.values())


