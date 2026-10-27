class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        op = [1] * len(nums)
        
        n=1
        for i in range(0,len(nums)):
            op[i] = op[i] * n
            n = n*nums[i]
        
        n=1
        for i in range(len(nums)-1,-1,-1):
            op[i] = op[i] * n
            n = n*nums[i]
        
        return op