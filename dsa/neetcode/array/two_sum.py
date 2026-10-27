class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = {}
        for i,v in enumerate(nums):
            diff = target - v
            if diff in sum:
                return [sum[diff],i]
            sum[v] = i