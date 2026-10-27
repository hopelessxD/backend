from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        check = defaultdict(list)

        for s in strs:
            sor = tuple(sorted(s))
            check[sor].append(s)
        
        return list(check.values())