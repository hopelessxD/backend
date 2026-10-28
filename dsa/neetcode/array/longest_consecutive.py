class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        length = 0
        for start in nums:
            if start-1 not in s:
                end = start+1
                while end in s:
                    end += 1
                length = max(length, end-start)
        return length
        