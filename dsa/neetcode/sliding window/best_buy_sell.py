class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        diff = 0
        res = 0
        m = prices[0]
        for i in range(len(prices)):
            m = min(m,prices[i])
            diff = prices[i] - m
            res = max(diff,res)
        return res