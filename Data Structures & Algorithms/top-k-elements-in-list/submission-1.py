from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        freq = Counter(nums)
        values = list(freq.values())
        sorted_values = sorted(values, reverse=True)
        keys = list(freq.keys())
        
        count = 0
        used = set()
        for val in sorted_values:
            for key in keys:
                if freq[key] == val and key not in used:
                    result.append(key)
                    used.add(key)
                    count +=1
                    if count == k:
                        return result
        
        return result
                    