class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        _hash = {}
        a = sorted(nums)
        new_list = []

        for i in a:
            if i in _hash:
                _hash[i] += 1
            else:
                _hash[i] = 1
        for i in range(k):
            key = max(_hash, key=_hash.get)
            if k != 0:
                new_list.append(key)
                _hash.pop(key)

        return list(new_list)