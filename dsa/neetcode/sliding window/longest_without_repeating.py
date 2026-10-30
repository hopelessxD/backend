class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxs = 0
        m = {}
        for right in range(len(s)):
            if s[right] in m:
                left = max(left,m[s[right]]+1)
            m[s[right]] = right
            maxs = max(maxs, right-left+1)
        return maxs