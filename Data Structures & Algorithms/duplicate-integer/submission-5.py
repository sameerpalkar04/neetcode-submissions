class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import Counter

        count = Counter(nums)
        for key in count:
            if count[key]>1:
                return True
        return False