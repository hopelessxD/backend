class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        check = {}
        op = []

        for i in nums:
            check[i] = check.get(i, 0) + 1
        
        sor = sorted(check.items(), key =lambda x: x[1], reverse = True)

        for i in sor[:k]:
            op.append(i[0])
        
        return op