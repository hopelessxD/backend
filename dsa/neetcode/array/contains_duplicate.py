class Solution:
    def hasDuplicate(self, nums) -> bool:
        if len(nums) == len(set(nums)):
            return False
        else:
            return True