class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicate = []
        flag = 0
        if len(nums) != 0:
            for i in range(len(nums)):
                if nums[i] not in duplicate:
                    duplicate.append(nums[i])
                    flag = 1
                else:
                    flag = 0
                    break
            
            if flag == 0:
                return True
            else:
                return False
        else:
            return False
